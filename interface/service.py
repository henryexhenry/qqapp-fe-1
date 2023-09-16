"""
import requests

base_url = "http://127.0.0.1:8000/api/"

def get_students():
    response = requests.get(base_url)
    return response.json()

    [
    {
        "id": 1,
        "name": "小王1",
        "age": 6,
        "level": "二级",
        "wechat_name": "hy",
        "parent_name": "",
        "start_learning_date": "2023-01-01",
        "experience_years": 1
    }
]

def create_student(student_data):
    response = requests.post(base_url, json=student_data)
    return response.json()

def update_student(student_id, student_data):
    url = f"{base_url}/{student_id}/"
    response = requests.put(url, json=student_data)
    return response.json()

def delete_student(student_id):
    url = f"{base_url}/{student_id}/"
    response = requests.delete(url)
    return response.json()



def get_lessons():
    response = requests.get(base_url)
    return response.json()

def create_lesson(lesson_data):
    response = requests.post(base_url, json=lesson_data)
    return response.json()

def update_lesson(lesson_id, lesson_data):
    url = f"{base_url}/{lesson_id}/"
    response = requests.put(url, json=lesson_data)
    return response.json()

def delete_lesson(lesson_id):
    url = f"{base_url}/{lesson_id}/"
    response = requests.delete(url)
    return response.json()
"""

from datetime import datetime
import api

DATEFORMAT = '%Y-%m-%d'

class qqapp:
    def add_student(self, ):
        api.create_student

# deserialize json to python object
class Student:
    def __init__(self, id, name, age, level, wechat_name, parent_name, start_learning_date, experience_years):
        self.id:int = id
        self.name:str = name
        self.age:int = age
        self.level:str = level
        self.wechat_name:str = wechat_name
        self.parent_name:str = parent_name
        self.start_learning_date:datetime = datetime.strptime(start_learning_date, DATEFORMAT)
        self.experience_years:int = experience_years
    
    def __str__(self):
        return f"Student(id={self.id}, name={self.name}, age={self.age}, level={self.level}, wechat_name={self.wechat_name}, parent_name={self.parent_name}, start_learning_date={self.start_learning_date}, experience_years={self.experience_years})"
    
    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, age={self.age}, level={self.level}, wechat_name={self.wechat_name}, parent_name={self.parent_name}, start_learning_date={self.start_learning_date}, experience_years={self.experience_years})"
    
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.age == other.age and self.level == other.level and self.wechat_name == other.wechat_name and self.parent_name == other.parent_name and self.start_learning_date == other.start_learning_date and self.experience_years == other.experience_years
    
    def __hash__(self):
        return hash((self.id, self.name, self.age, self.level, self.wechat_name, self.parent_name, self.start_learning_date, self.experience_years))
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "level": self.level,
            "wechat_name": self.wechat_name,
            "parent_name": self.parent_name,
            "start_learning_date": self.start_learning_date,
            "experience_years": self.experience_years,
        }
    
    def deserialize(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.age = data["age"]
        self.level = data["level"]
        self.wechat_name = data["wechat_name"]
        self.parent_name = data["parent_name"]
        self.start_learning_date = data["start_learning_date"]
        self.experience_years = data["experience_years"]
        return self
    
"""
learning-info
{
    "id": 1,
    "enrollment_date": "2023-08-19",
    "total_consumed_hours": 0,
    "remaining_hours": 0,
    "class_frequency": null,
    "student": 1
}
"""

# deserialize json to python object

class LearningInfo:
    def __init__(self, id, enrollment_date, total_consumed_hours, remaining_hours, class_frequency, student_id):
        self.id:int = id
        self.enrollment_date: datetime = enrollment_date
        self.total_consumed_hours: int = total_consumed_hours
        self.remaining_hours:int = remaining_hours
        self.class_frequency:str = class_frequency
        self.student_id:int = student_id

    def __str__(self):
        return f"LearningInfo(id={self.id}, enrollment_date={self.enrollment_date}, total_consumed_hours={self.total_consumed_hours}, remaining_hours={self.remaining_hours}, class_frequency={self.class_frequency}, student={self.student_id})"
    
    def __repr__(self):
        return f"LearningInfo(id={self.id}, enrollment_date={self.enrollment_date}, total_consumed_hours={self.total_consumed_hours}, remaining_hours={self.remaining_hours}, class_frequency={self.class_frequency}, student_id={self.student_id})"
    
    def __eq__(self, other):
        return self.id == other.id and self.enrollment_date == other.enrollment_date and self.total_consumed_hours == other.total_consumed_hours and self.remaining_hours == other.remaining_hours and self.class_frequency == other.class_frequency and self.student_id == other.student_id
    
    def __hash__(self):
        return hash((self.id, self.enrollment_date, self.total_consumed_hours, self.remaining_hours, self.class_frequency, self.student_id))
    
    def serialize(self):
        return {
            "id": self.id,
            "enrollment_date": self.enrollment_date,
            "total_consumed_hours": self.total_consumed_hours,
            "remaining_hours": self.remaining_hours,
            "class_frequency": self.class_frequency,
            "student": self.student_id,
        }
    
    def deserialize(self, data):
        self.id = data["id"]
        self.enrollment_date = data["enrollment_date"]
        self.total_consumed_hours = data["total_consumed_hours"]
        self.remaining_hours = data["remaining_hours"]
        self.class_frequency = data.get("class_frequency")
        self.student_id = data["student"]
        return self
    