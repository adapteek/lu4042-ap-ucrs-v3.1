from pydantic import BaseModel , Field

class StudentCreate(BaseModel):
    first_name: str | None = Field(..., min_length=2, max_length=50, pattern=r"^[A-Za-z ]+$", examples = ["Mohammad"])
    last_name: str | None = Field(..., min_length=2, max_length=50, pattern=r"^[A-Za-z ]+$", examples = ["Zareian"])
    student_number: str | None = Field(..., min_length=3, max_length=30, pattern=r"^[0-9]+$", examples = ["40411415058"])
    major: str | None = Field(..., min_length=2, max_length=80, pattern=r"^[A-Za-z ]+$", examples = ["Computer Engineering"])

class StudentUpdate(BaseModel):
    first_name: str | None = Field(default = None, min_length=2, max_length=50, pattern=r"^[A-Za-z ]+$")
    last_name: str | None = Field(default = None, min_length=2, max_length=50, pattern=r"^[A-Za-z ]+$")
    student_number: str | None = Field(default = None, min_length=3, max_length=30, pattern=r"^[0-9]+$")
    major: str | None = Field(default = None, min_length=2, max_length=80, pattern=r"^[A-Za-z ]+$")