from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from exceptions.custom_exceptions import (
    CourseSelectionException,
    CourseNotFoundException,
    CourseAlreadySelectedException,
    CourseNotSelectedException,
    CourseFullException,
    ProfessorAlreadyAssignedException,
    ProfessorNotFoundException,
    StudentNotFoundException,
    InvalidDataExceptions,
)
from routers.professors import router as professors_router
from routers.students import router as students_router
from routers.courses import router as courses_router
from data.storage import load_all, _save_all, students, professors, courses


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_all()
    yield
    _save_all()


app = FastAPI(
    title="University Course Registration System",
    description="API for managing courses, professors, and students in a university setting.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(professors_router)
app.include_router(students_router)
app.include_router(courses_router)


@app.get("/")
def root():
    return {"message": "به سیستم انتخاب واحد خوش آمدید"}


@app.get("/debug/storage", tags=["Debug"])
def debug_storage_summary():
    return {
        "students_count": len(students),
        "professors_count": len(professors),
        "courses_count": len(courses),
    }


@app.get("/debug/storage/all", tags=["Debug"])
def debug_storage_all():
    return {
        "students": [student.to_dict() for student in students.values()],
        "professors": [professor.to_dict() for professor in professors.values()],
        "courses": [course.to_dict() for course in courses.values()],
    }


@app.exception_handler(CourseNotFoundException)
async def course_not_found_exception_handler(request: Request, exc: CourseNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": str(exc)})


@app.exception_handler(StudentNotFoundException)
async def student_not_found_exception_handler(request: Request, exc: StudentNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": str(exc)})


@app.exception_handler(ProfessorNotFoundException)
async def professor_not_found_exception_handler(request: Request, exc: ProfessorNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": str(exc)})


@app.exception_handler(
    CourseAlreadySelectedException
)
async def course_already_selected_exception_handler(request: Request, exc: CourseAlreadySelectedException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(exc)})


@app.exception_handler(CourseNotSelectedException)
async def course_not_selected_exception_handler(request: Request, exc: CourseNotSelectedException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(exc)})


@app.exception_handler(CourseFullException)
async def course_full_exception_handler(request: Request, exc: CourseFullException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(exc)})


@app.exception_handler(ProfessorAlreadyAssignedException)
async def professor_already_assigned_exception_handler(
    request: Request, exc: ProfessorAlreadyAssignedException
):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(exc)})


@app.exception_handler(InvalidDataExceptions)
async def invalid_data_exception_handler(request: Request, exc: InvalidDataExceptions):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(exc)})


@app.exception_handler(CourseSelectionException)
async def course_selection_exception_handler(request: Request, exc: CourseSelectionException):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(exc)})
