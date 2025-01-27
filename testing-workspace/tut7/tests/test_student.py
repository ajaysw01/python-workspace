from datetime import datetime
from app.student import  get_topper

# Tests
def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age

def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 20

def test_get_topper(student_factory):
    students = [
        student_factory("ram", 21),
        student_factory("ajay", 32),
    ]
    topper = get_topper(students)
    assert topper == students[1]  # 'ajay' has the highest credits