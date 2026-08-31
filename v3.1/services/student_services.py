from schemas.student_schema import StudentCreate, StudentUpdate
from models.student import Student
from data.storage import students, get_next_student_id, _save_all
from exceptions.custom_exceptions import InvalidDataExceptions, StudentNotFoundException


def create_student(student_data: StudentCreate) -> Student:
    if any(student.student_number == student_data.student_number for student in students.values()):
        raise InvalidDataExceptions("شماره دانشجویی تکراری است")

    student = Student(
        id=get_next_student_id(),
        first_name=student_data.first_name,
        last_name=student_data.last_name,
        student_number=student_data.student_number,
        major=student_data.major,
    )
    students[student.id] = student
    _save_all()
    return student


def get_all_students():
    return list(students.values())


def get_student_by_id(student_id: int) -> Student:
    student = students.get(student_id)
    if student is None:
        raise StudentNotFoundException("دانشجو پیدا نشد")
    return student


def update_student(student_id: int, student_data: StudentUpdate) -> Student:
    student = get_student_by_id(student_id)

    if student_data.student_number is not None:
        duplicate = any(
            s.id != student_id and s.student_number == student_data.student_number
            for s in students.values()
        )
        if duplicate:
            raise InvalidDataExceptions("شماره دانشجویی تکراری است")
        student.student_number = student_data.student_number

    if student_data.first_name is not None:
        student.first_name = student_data.first_name
    if student_data.last_name is not None:
        student.last_name = student_data.last_name
    if student_data.major is not None:
        student.major = student_data.major

    _save_all()
    return student


def delete_student(student_id: int) -> None:
    student = get_student_by_id(student_id)

    for course in list(student.selected_courses):
        course.remove_student(student)
        student.selected_courses.remove(course)

    del students[student_id]
    _save_all()
