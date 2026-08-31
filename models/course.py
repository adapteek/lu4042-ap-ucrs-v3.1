from exceptions.custom_exceptions import (
    CourseAlreadySelectedException,
    CourseFullException,
    CourseNotSelectedException,
    ProfessorAlreadyAssignedException,
)


class Course:
    def __init__(
        self,
        id: int,
        title: str,
        code: str,
        major: str,
        unit: int,
        capacity: int,
    ):
        self.id = id
        self.title = title
        self.code = code
        self.major = major
        self.unit = unit
        self.capacity = capacity
        self.professor = None
        self.students = []

    def is_full(self) -> bool:
        return len(self.students) >= self.capacity

    def add_student(self, student):
        if student in self.students:
            raise CourseAlreadySelectedException("درس قبلا توسط دانشجو انتخاب شده است")
        if self.is_full():
            raise CourseFullException("ظرفیت این درس پر است")
        self.students.append(student)

    def remove_student(self, student):
        if student not in self.students:
            raise CourseNotSelectedException("دانشجو قبلا در این درس ثبت نام نکرده است")
        self.students.remove(student)

    def professor_assignment(self, professor):
        if self.professor is not None:
            if self.professor.id == professor.id:
                raise ProfessorAlreadyAssignedException(
                    "این درس قبلا به این استاد تخصیص داده شده است"
                )
            raise ProfessorAlreadyAssignedException("این درس قبلا استاد دارد")

        self.professor = professor
        professor.assign_course(self)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "code": self.code,
            "major": self.major,
            "unit": self.unit,
            "capacity": self.capacity,
            "remaining_capacity": self.capacity - len(self.students),
            "professor": None if self.professor is None else {
                "id": self.professor.id,
                "first_name": self.professor.first_name,
                "last_name": self.professor.last_name,
                "personnel_code": self.professor.personnel_code,
            },
            "students": [
                {
                    "id": student.id,
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "student_number": student.student_number,
                }
                for student in self.students
            ],
        }
