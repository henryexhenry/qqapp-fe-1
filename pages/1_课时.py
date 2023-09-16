import streamlit as st
import pandas as pd
import queue
import datetime
from config import AppConfiguration
from service.swagger_client.api.course_api import CourseApi
from service.swagger_client.api.lesson_op_api import LessonOpApi
from service.swagger_client.api_client import ApiClient
from service.swagger_client.models import *



st.set_page_config(page_title="qqapp-课时", page_icon="📈")

# 初始化
msg = st.empty()

if st.session_state.get('LOADING') is None:
    st.session_state['LOADING'] = False
if st.session_state.get('Q_EVENT') is None:
    st.session_state['Q_EVENT']:queue.Queue = queue.Queue()


st.sidebar.header("课时")

# load data
api_client = ApiClient(AppConfiguration())
course_api = CourseApi(api_client)
lesson_op_api = LessonOpApi(api_client)
client_courses:list[Course] = course_api.course_list().results


def click_event(course, action):
    st.session_state['LOADING'] = True
    st.session_state['Q_EVENT'].put((course, action, None))

def birth2age(birth_date):
    if not birth_date:
        return None
    return (datetime.datetime.now() - birth_date.replace(tzinfo=None)).days // 365


"""
# 课时信息
---
"""
st.json([cc.to_dict() for cc in client_courses], expanded=False)
for course in client_courses:
    client = course.client

    # 课时信息
    col0, col1, col2, col3 = st.columns([5,5,5,3])
    col0.markdown(f'### {client.client_name}')
    col0.markdown(f'*{client.wechat_id}  ( { birth2age(client.birthday) }岁 )*')
    col1.markdown('')
    col1.metric("消耗课时", course.total_consumed_lessons)
    col2.markdown('')
    col2.metric("剩余课时", course.remaining_lessons)
    with col3:
        col3.markdown('')
        col3.markdown('')
        st.button(
            key=f'{course.id}-consume',
            label='消课', 
            on_click=click_event, 
            args=(course,'consume'),
            disabled=st.session_state['LOADING'],
        )

    # 课时记录詳情
    with st.expander("records", expanded=False):
        record_list = lesson_op_api.lesson_op_list(course=course.id).results
        if len(record_list) == 0:
            st.markdown('暂无记录')
            continue
        df = pd.DataFrame.from_records([r.__dict__ for r in record_list])
        df['_create_time'] = df['_create_time'].dt.tz_convert('Asia/Shanghai').dt.strftime('%Y-%m-%d %H:%M:%S')
        df['course_name'] = df['_course'].map(lambda c: c.course_name)
        df['_op_type'] = df['_op_type'].map({1: '充值', 0: '消课'})
        df = df.set_index('_create_time').sort_index(ascending=False)
        del df['_course']
        del df['_id']
        st.table(df[['course_name', '_op_type', '_lessons']])


while not st.session_state['Q_EVENT'].empty():
    course: Course
    course, action, data = st.session_state['Q_EVENT'].get()
    if action == 'consume':
        # 處理消課操作
        try:
            lesson_op_api.lesson_op_create(body=LessonOpLog(course=course.id, op_type=0,lessons=1))
            st.session_state['Q_EVENT'].put((course, "consume_success", None))
            print(f"{course.course_name} consumed")
        except Exception as e:
            st.session_state['Q_EVENT'].put((course, "consume_failed", e.body))
        st.session_state['LOADING'] = False
        st.experimental_rerun()
    elif action == 'consume_success':
        msg.success(f"{course.course_name} 消课成功")
    elif action == 'consume_failed':
        msg.error(f"{course.course_name} 消课失败: {data}")
        

