import streamlit as st
import time
import numpy as np
from interface import api

st.set_page_config(page_title="qqapp-学生注册", page_icon="📈")

st.sidebar.header("学生注册")

msg = st.empty()


with st.form(key="student"):
    st.markdown('## 学生注册')
    st.markdown('---')
    col1, col2 = st.columns([1,1])
    with col1:
        student_name = st.text_input(
            label="学生名称", 
            key='student_name', 
            placeholder="必填")
        wechat_name = st.text_input(
            label="微信名", 
            key='wechat_name', 
            placeholder="必填")
        age = st.number_input(
            label="学生年龄", 
            step=1,
            key='age')
        level = st.text_input(
            label="学生级别", 
            key='level', 
            placeholder="选填")
    with col2:
        parent_name = st.text_input(
            label="家长姓名", 
            key='parent_name', 
            placeholder="选填")
        start_learning_date = st.date_input(
            label="开始学习日期",
            key='start_learning_date',
            value=None,
            help="选填")
        lesson_price = st.number_input(
            label="课时单价",
            min_value=50,
            max_value=1000,
            value=300,
            step=50,
            key='lesson_price',
            help="选填")
        lesson_freq_per_week = st.number_input(
            label="每周几次课",
            min_value=1,
            max_value=100,
            value=2,
            step=1,
            key='lesson_freq_per_week',
            help="选填")

    submitted = st.form_submit_button(label="注册")
    if submitted:
        res = api.create_student({
            "name": student_name,
            "wechat_name": wechat_name,
            "age": age,
            "level": level,
            "parent_name": parent_name,
            "start_learning_date": start_learning_date.strftime('%Y-%m-%d') if start_learning_date else None,
            "lesson_price": lesson_price,
            "lesson_freq_per_month": lesson_freq_per_week * 4,
        })
        if res.get('id'):
            msg.success(f'注册成功: {res.get("name")}')
        else:
            msg.error(f'注册失败: {res.get("detail")}')


    st.json(body={
            "name": student_name,
            "wechat_name": wechat_name,
            "age": age,
            "level": level,
            "parent_name": parent_name,
            "start_learning_date": start_learning_date.strftime('%Y-%m-%d') if start_learning_date else None,
            "lesson_price": lesson_price,
            "lesson_freq_per_month": lesson_freq_per_week * 4,
        }, expanded=False)