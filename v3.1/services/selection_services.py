from services.student_services import get_student_by_id
from services.professor_services import get_professor_by_id
from services.course_services import get_course_by_id
from data.storage import _save_all


def select_course_for_student(student_id: int, course_id: int):
    student = get_student_by_id(student_id)
    course = get_course_by_id(course_id)
    course.add_student(student)
    student.select_course(course)
    _save_all()
    return student


def drop_course_for_student(student_id: int, course_id: int):
    student = get_student_by_id(student_id)
    course = get_course_by_id(course_id)
    course.remove_student(student)
    student.drop_course(course)
    _save_all()
    return student


def get_selected_courses_for_student(student_id: int):
    student = get_student_by_id(student_id)
    return student.get_courses()


def assign_professor_to_course(professor_id: int, course_id: int):
    course = get_course_by_id(course_id)
    professor = get_professor_by_id(professor_id)
    course.professor_assignment(professor)
    _save_all()
    return course
