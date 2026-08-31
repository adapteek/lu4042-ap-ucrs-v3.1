from pydantic import BaseModel , Field

class ProfessorCreate(BaseModel):
    first_name: str | None = Field(..., min_length=2, max_length=50, pattern=r"^[A-Za-z ]+$", examples = ["Armin"])
    last_name: str | None = Field(..., min_length=2, max_length=50, pattern=r"^[A-Za-z ]+$", examples = ["Rashno"])
    personnel_code: str | None = Field(..., min_length=3, max_length=30, pattern=r"^[0-9]+$", examples = ["138715053"])
    department: str | None = Field(..., min_length=2, max_length=80, pattern=r"^[A-Za-z ]+$", examples = ["Computer"])

class ProfessorUpdate(BaseModel):
    first_name: str | None = Field(default = None, min_length=2, max_length=50, pattern=r"^[A-Za-z ]+$")
    last_name: str | None = Field(default = None, min_length=2, max_length=50, pattern=r"^[A-Za-z ]+$")
    personnel_code: str | None = Field(default = None, min_length=3, max_length=30, pattern=r"^[0-9]+$")
    department: str | None = Field(default = None, min_length=2, max_length=80, pattern=r"^[A-Za-z ]+$")