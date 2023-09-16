import requests
import streamlit as st
from datetime import datetime


base_url = "http://127.0.0.1:8000/api"

student_endpoint = f"{base_url}/students/"
learning_info_endpoint = f"{base_url}/learning-info"
lesson_record_endpoint = f"{base_url}/lesson-records"


"""
CRUD students
"""
def handle_response(response):
    try:
        res = response.json()
        return res
    except BaseException as e:
        print(e)
        raise response.text

st.cache_data()
def get_students():
    response = requests.get(student_endpoint)
    return handle_response(response)

def create_student(student_data):
    response = requests.post(student_endpoint, json=student_data)
    return handle_response(response)

def update_student(student_id, student_data):
    response = requests.put(f"{student_endpoint}/{student_id}", json=student_data)
    return handle_response(response)

def delete_student(student_id):
    url = f"{student_endpoint}/{student_id}/"
    response = requests.delete(url)
    return handle_response(response)




"""
CRUD lesson records
"""

def get_lesson_records(student_id):
    response = requests.get(f"{lesson_record_endpoint}?student={student_id}")
    return handle_response(response).get('results')

def purchase_lesson(student_id, lessons, payment, comment):
    data = {
        "student": student_id,
        "action": "purchase",
        "lessons": lessons,
        "payment": payment,
        "comment": comment
    }
    response = requests.post(lesson_record_endpoint+'/', json=data)
    return handle_response(response)

def consume_lesson(student_id, comment=None):
    data = {
        "student": student_id,
        "action": "consume",
        "lessons": 1,
        "comment": comment
    }
    response = requests.post(lesson_record_endpoint+'/', json=data)
    return handle_response(response)