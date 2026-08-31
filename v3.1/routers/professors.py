from fastapi import APIRouter, status
from schemas.professor_schema import ProfessorUpdate, ProfessorCreate
from services.professor_services import (
    create_professor,
    update_professor,
    delete_professor,
    get_all_professors,
    get_professor_by_id,
)

router = APIRouter(prefix="/professors", tags=["Professors"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_new_professor(professor: ProfessorCreate):
    return create_professor(professor).to_dict()


@router.get("/")
def list_professors():
    return [professor.to_dict() for professor in get_all_professors()]


@router.get("/{professor_id}")
def retrieve_professor(professor_id: int):
    return get_professor_by_id(professor_id).to_dict()


@router.put("/{professor_id}")
def edit_professor(professor_id: int, professor: ProfessorUpdate):
    return update_professor(professor_id, professor).to_dict()


@router.delete("/{professor_id}", status_code=status.HTTP_200_OK)
def remove_professor(professor_id: int):
    delete_professor(professor_id)
    return {"message": "استاد با موفقیت حذف شد."}
