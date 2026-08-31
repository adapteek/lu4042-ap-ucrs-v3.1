from schemas.professor_schema import ProfessorCreate, ProfessorUpdate
from models.professor import Professor
from data.storage import professors, get_next_professor_id, _save_all
from exceptions.custom_exceptions import InvalidDataExceptions, ProfessorNotFoundException

def create_professor(professor_data: ProfessorCreate) -> Professor:
    if any(professor.personnel_code == professor_data.personnel_code for professor in professors.values()):
        raise InvalidDataExceptions("کد پرسنلی تکراری است")

    professor = Professor(
        id=get_next_professor_id(),
        first_name=professor_data.first_name,
        last_name=professor_data.last_name,
        personnel_code=professor_data.personnel_code,
        department=professor_data.department,
    )
    professors[professor.id] = professor
    _save_all()
    return professor

def get_all_professors():
    return list(professors.values())

def get_professor_by_id(professor_id : int) -> Professor:
    professor = professors.get(professor_id)
    if professor is None:
        raise ProfessorNotFoundException("استاد پیدا نشد")
    return professor

def update_professor(professor_id: int, professor_data: ProfessorUpdate) -> Professor:
    professor = professors.get(professor_id)

    if professor_data.personnel_code is not None:
        duplicate=any(
            p.id != professor_id and p.personnel_code == professor_data.personnel_code
            for p in professors.values()
        )
        if duplicate:
            raise InvalidDataExceptions("کد پرسنلی استاد تکراری است")
        professor.personnel_code=professor_data.personnel_code

    if professor_data.first_name is not None:
        professor.first_name = professor_data.first_name
    if professor_data.last_name is not None:
        professor.last_name = professor_data.last_name
    if professor_data.department is not None:
        professor.department = professor_data.department

    _save_all()
    return professor

def delete_professor(professor_id: int) -> None:
    professor = get_professor_by_id(professor_id)

    for course in list(professor.courses):
        if course.professor is not None and course.professor.id == professor_id:
            course.professor = None

    del professors[professor_id]
    _save_all()