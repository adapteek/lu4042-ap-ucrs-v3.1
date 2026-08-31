from fastapi import APIRouter, status
from schemas.student_schema import StudentUpdate, StudentCreate
from services.student_services import (
    create_student,
    update_student,
    delete_student,
    get_all_students,
    get_student_by_id,
)
from services.selection_services import (
    select_course_for_student as select_course_service,
    drop_course_for_student as drop_course_service,
    get_selected_courses_for_student,
)

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_new_student(student: StudentCreate):
    return create_student(student).to_dict()


@router.get("/")
def list_students():
    return [student.to_dict() for student in get_all_students()]


@router.get("/{student_id}")
def retrieve_student(student_id: int):
    return get_student_by_id(student_id).to_dict()


@router.put("/{student_id}")
def edit_student(student_id: int, student: StudentUpdate):
    return update_student(student_id, student).to_dict()


@router.delete("/{student_id}", status_code=status.HTTP_200_OK)
def remove_student(student_id: int):
    delete_student(student_id)
    return {"message": "دانشجو با موفقیت حذف شد."}


@router.get("/{student_id}/courses")
def retrieve_student_courses(student_id: int):
    courses = get_selected_courses_for_student(student_id)
    return [course.to_dict() for course in courses]


@router.post("/{student_id}/courses/{course_id}")
def select_course(student_id: int, course_id: int):
    student = select_course_service(student_id, course_id)
    return {
        "message": "درس با موفقیت برای دانشجو انتخاب شد.",
        "student": student.to_dict(),
    }


@router.delete("/{student_id}/courses/{course_id}")
def drop_course(student_id: int, course_id: int):
    student = drop_course_service(student_id, course_id)
    return {
        "message": "درس با موفقیت از انتخاب دانشجو حذف شد.",
        "student": student.to_dict(),
    }
