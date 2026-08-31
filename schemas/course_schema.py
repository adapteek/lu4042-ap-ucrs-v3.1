from pydantic import BaseModel, Field


class CourseCreate(BaseModel):
    major: str | None = Field(None, min_length=2, max_length=80, pattern=r"^[A-Za-z ]+$", examples=["Computer Engineering"])
    title: str | None = Field(None, min_length=2, max_length=100, pattern=r"^[A-Za-z ]+$", examples=["Data Structure and Algorithmes"])
    code: str | None = Field(None, min_length=2, max_length=20, pattern=r"^[A-Za-z0-9]+$", examples=["DSA105"])
    unit: int | None = Field(None, ge=1, le=5, examples=[3])
    capacity: int | None = Field(None, ge=1, le=200, examples=[30])


class CourseUpdate(BaseModel):
    major: str | None = Field(default=None, min_length=2, max_length=80, pattern=r"^[A-Za-z ]+$")
    title: str | None = Field(default=None, min_length=2, max_length=100, pattern=r"^[A-Za-z ]+$")
    code: str | None = Field(default=None, min_length=2, max_length=20, pattern=r"^[A-Za-z0-9]+$")
    unit: int | None = Field(default=None, ge=1, le=5)
    capacity: int | None = Field(default=None, ge=1, le=200)
