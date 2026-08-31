from data.storage import courses, get_next_course_id, _save_all
from exceptions.custom_exceptions import InvalidDataExceptions, CourseNotFoundException
from models.course import Course
from schemas.course_schema import CourseCreate, CourseUpdate


def create_course(course_data: CourseCreate) -> Course:
    if any(course.code == course_data.code for course in courses.values()):
        raise InvalidDataExceptions("کد درس تکراری است")

    course = Course(
        id=get_next_course_id(),
        title=course_data.title,
        code=course_data.code,
        major=course_data.major,
        unit=course_data.unit,
        capacity=course_data.capacity,
    )
    courses[course.id] = course
    _save_all()
    return course


def get_all_courses() -> list[Course]:
    return list(courses.values())


def get_course_by_id(course_id: int) -> Course:
    course = courses.get(course_id)
    if course is None:
        raise CourseNotFoundException("درس پیدا نشد")
    return course


def update_course(course_id: int, course_data: CourseUpdate) -> Course:
    course = get_course_by_id(course_id)

    if course_data.code is not None:
        duplicate = any(
            c.id != course_id and c.code == course_data.code
            for c in courses.values()
        )
        if duplicate:
            raise InvalidDataExceptions("کد درس تکراری است")
        course.code = course_data.code

    if course_data.capacity is not None:
        if course_data.capacity < len(course.students):
            raise InvalidDataExceptions(
                "ظرفیت جدید نمیتواند کمتر از تعداد دانشجویان ثبت نام کننده باشد"
            )
        course.capacity = course_data.capacity

    if course_data.title is not None:
        course.title = course_data.title
    if course_data.major is not None:
        course.major = course_data.major
    if course_data.unit is not None:
        course.unit = course_data.unit

    _save_all()
    return course


def delete_course(course_id: int) -> None:
    course = get_course_by_id(course_id)

    for student in list(course.students):
        if course in student.selected_courses:
            student.selected_courses.remove(course)
        course.students.remove(student)

    if course.professor is not None and course in course.professor.courses:
        course.professor.courses.remove(course)

    del courses[course_id]
    _save_all()
