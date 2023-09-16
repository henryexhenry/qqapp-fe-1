
from config import AppConfiguration
from service.swagger_client.api.class_session_api import ClassSessionApi
from service.swagger_client.api_client import ApiClient
from service.swagger_client.models import *
from service.swagger_client.api.course_api import CourseApi
from calendarHelper import CALENDAR_MODE, build_option, classs2event4daygrid, classs2event4timegrid

import streamlit as st
from streamlit_calendar import calendar
from streamlit_autorefresh import st_autorefresh
import copy
import time
import queue
import datetime
print('top')

st.set_page_config(page_title="qqapp-排课", page_icon="📈")


# 初始化
msg = st.empty()

if st.session_state.get('LOADING') is None:
    st.session_state['LOADING'] = False
if st.session_state.get('Q_EVENT') is None:
    st.session_state['Q_EVENT']:queue.Queue = queue.Queue()


st.sidebar.header("排课")
sidebar_placeholder_1 = st.sidebar.empty()
sidebar_placeholder_2 = st.sidebar.empty()


"""
# 排课
---
"""


api_client = ApiClient(AppConfiguration())
course_api = CourseApi(api_client)
clssss_api = ClassSessionApi(api_client)

client_courses:list[Course] = course_api.course_list().results

mode = st.selectbox(
    "Calendar Mode:",
    CALENDAR_MODE,
)

clssss_list = clssss_api.class_session_list(page=1, page_size=1000).results
if mode == "daygrid":
    clssss_list = list(map(classs2event4daygrid, clssss_list))
else: #if mode == "timegrid":
    clssss_list = list(map(classs2event4timegrid, clssss_list))

options = build_option(mode)
st.json(options, expanded=False)
state = calendar(
    events=clssss_list,
    options=options,
    key=mode,
)

st.json(st.session_state, expanded=False)



class CalendarEventHandler:
    def __init__(self, cls_session_api:ClassSessionApi):
        self.cls_session_api = cls_session_api    

    # 指定时间后, 创建 lesson session
    def handle_date_click(self, date_click, client_courses):
        print('date click')

        form = sidebar_placeholder_1.form(key="sidebar_placeholder_1")
        col1_, col2_ = form.columns([1,4])
        course = col2_.selectbox(label="课程", options=client_courses, format_func=lambda x: x.course_name)
        color = col1_.color_picker(label="vvv", key='color', value=course.color, disabled=True)
        start_datetime = datetime.datetime.fromisoformat(date_click.get('dateStr'))
        start_date = form.date_input(label="startdate", value=start_datetime)
        start_time = form.time_input(label="starttime", value=start_datetime)
        lessons = form.number_input(label="课时", min_value=1, max_value=5, value=1, step=1)
        comment = form.text_area(label="备注", value="微信轉帳", help="选填")
        end_datetime = datetime.datetime.combine(start_date,start_time)  + datetime.timedelta(minutes=lessons * course.class_length)

        create_button = form.form_submit_button(label="创建")
        if create_button:
            res:ClassSession = self.cls_session_api.class_session_create(body=ClassSession(
                course=course.id,
                start_time=start_datetime,
                end_time=end_datetime,
                lessons=lessons,
                comment=comment
            ))
            if res.id:
                msg.success(f'创建成功: {course.course_name} 课时: {lessons}')
                sidebar_placeholder_1.empty()
            else:
                msg.warning(f'创建失败: {res.get("detail")}')


    # 展示 lesson detail
    def handle_event_click(self, event_click):
        print('event click')

        form = sidebar_placeholder_1.form(key="sidebar_placeholder_1")
        col1_, col2_ = form.columns([1,4])
        col2_.header(event_click.get('event').get('title'))
        color = col1_.color_picker(label="vvv", key='color', value=event_click.get('event').get('backgroundColor'), disabled=True)
        start_datetime = datetime.datetime.fromisoformat(event_click.get('event').get('start'))
        start_date = form.date_input(label="startdate", value=start_datetime)
        start_time = form.time_input(label="starttime", value=start_datetime)
        lessons = form.number_input(label="课时", min_value=1, max_value=5, value=event_click.get('event').get('extendedProps').get('lessons'), step=1)
        comment = form.text_area(label="备注", value=event_click.get('event').get('extendedProps').get('comment'), help="选填")
        end_datetime = datetime.datetime.combine(start_date,start_time) \
            + datetime.timedelta(minutes=lessons * event_click.get('event').get('extendedProps').get('class_length'))
        
        col1, col2 = form.columns([1,1])
        if col1.form_submit_button(label="编辑"):
            res:ClassSession = self.cls_session_api.class_session_update(
                id=event_click.get('event').get('id'),
                body=ClassSession(
                    course=event_click.get('event').get('extendedProps').get('course_id'),
                    start_time=start_datetime,
                    end_time=end_datetime,
                    lessons=lessons,
                    comment=comment
            ))
            if res.id:
                msg.success(f"编辑成功: {event_click.get('event').get('title')} 课时: {lessons}")
                sidebar_placeholder_1.empty()
            else:
                msg.warning(f'创建失败: {res.get("detail")}')
        if col2.form_submit_button(label="删除", type="secondary", help="删除后无法恢复"):
            self.cls_session_api.class_session_delete(id=event_click.get('event').get('id'))
            msg.success(f"删除成功: {event_click.get('event').get('title')} {event_click.get('event').get('start')}")
            sidebar_placeholder_1.empty()

        if sidebar_placeholder_2.button(label="消课", use_container_width=True):
            self.cls_session_api.class_session_eliminate_session(id=event_click.get('event').get('id'))
            msg.success(f"消课成功: {event_click.get('event').get('title')} 消课: {event_click.get('event').get('extendedProps').get('lessons')} 课时")

    # 修改 lesson session
    def handle_event_change(self, event_change):
        print('event change')

        res = self.cls_session_api.class_session_update(
            id=event_change.get('event').get('id'), 
            body=ClassSession(
                start_time=datetime.datetime.fromisoformat(event_change.get('event').get('start')),
                end_time=datetime.datetime.fromisoformat(event_change.get('event').get('end')),
                lessons=event_change.get('event').get('extendedProps').get('lessons'),
                comment=event_change.get('event').get('extendedProps').get('comment'),
                course=event_change.get('event').get('extendedProps').get('course_id'),
            ))
        if res.id:
            msg.success(f"修改成功: {event_change.get('event').get('title')}")
        else:
            msg.warning(f'修改失败: {res.get("detail")}')


ceh = CalendarEventHandler(cls_session_api=clssss_api)


if st.session_state.get(mode):
    mode_data = copy.deepcopy(st.session_state[mode])

    if mode_data.get('dateClick'):
        date_click = mode_data['dateClick']
        ceh.handle_date_click(date_click, client_courses)

    if mode_data.get('eventClick'):
        event_click = mode_data['eventClick']
        ceh.handle_event_click(event_click)
    
    if mode_data.get('eventChange'):
        event_change = mode_data['eventChange']
        ceh.handle_event_change(event_change)


