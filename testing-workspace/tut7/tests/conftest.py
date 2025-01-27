import pytest
from app.student import Student
from datetime import datetime

# Fixtures
@pytest.fixture
def dummy_student():
    return Student("nikhil", datetime(2000, 1, 1), "COE", 20)

@pytest.fixture
def student_factory():
    def make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "COE", credits)
    return make_dummy_student