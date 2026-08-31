from models.person import Person
from exceptions.custom_exceptions import (
    CourseAlreadySelectedException,
    CourseNotSelectedException
    )

class Student(Person) :
    def __init__(
            self,
            id: int,
            first_name: str,
            last_name: str,
            student_number: int,
            major: str
        ):
        super().__init__(id, first_name, last_name)
        self.student_number = student_number
        self.major = major
        self.selected_courses = []

    def select_course(self, course):
        if course in self.selected_courses:
            raise CourseAlreadySelectedException(
                "این درس قبلا توسط دانشجو انتخاب شده است"
                )
        self.selected_courses.append(course)
     
    def drop_course(self, course):
        if course not in self.selected_courses:
            raise CourseNotSelectedException(
                "درس توسط دانشجو انتخاب نشده است"
                )
        self.selected_courses.remove(course)

    def get_courses(self) -> list:
        return self.selected_courses

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "student_number": self.student_number,
            "major": self.major,
            "selected_courses": [
                {
                    "id": course.id,
                    "title": course.title,
                    "code": course.code,
                    "unit": course.unit
                }
                for course in self.selected_courses
            ]
        })
        return data