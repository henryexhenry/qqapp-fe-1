import streamlit as st
import time
import numpy as np
from config import AppConfiguration
from service.swagger_client.api.lesson_op_api import LessonOpApi
from service.swagger_client.api_client import ApiClient
from service.swagger_client.models import *
from service.swagger_client.api.course_api import CourseApi


st.set_page_config(page_title="qqapp-充值", page_icon="📈")

st.sidebar.header("充值")

msg = st.empty()


api_client = ApiClient(AppConfiguration())
cource_api = CourseApi(api_client)
lesson_op_api = LessonOpApi(api_client)

client_courses:list[Course] = cource_api.course_list().results

"""
充值
---
"""

with st.container():
    col1, col2 = st.columns([2,1])
    with col1:

        course:Course = st.selectbox(
            key='student', 
            label="选择学生", 
            options=client_courses, 
            format_func=lambda x: f"{x.course_name} ({x.client.wechat_id}) @{x.class_fee}元/课时")
        comment = st.text_input(
            label="备注", 
            key='comment', 
            value="微信轉帳", 
            placeholder="选填")
    with col2:
        lesson_count = st.number_input(
            label="充值课时",
            min_value=1,
            max_value=100,
            value=5, 
            step=1,
            key='lessons',
        )
        st.number_input(key="total", label="總金額",value=lesson_count * course.class_fee)
    submitted = st.button(label="充值", )
    if submitted:
        try:
            lesson_op_api.lesson_op_create(
                body=LessonOpLog(
                    lessons=lesson_count,
                    course=course.id,
                    op_type=1,
            ))
            msg.success(f'充值成功: {course.course_name} 课时: {lesson_count} 金额: {st.session_state["total"]}')
        except Exception as e:
            msg.error(f'充值失败: {e}')


st.json(st.session_state, expanded=False)

