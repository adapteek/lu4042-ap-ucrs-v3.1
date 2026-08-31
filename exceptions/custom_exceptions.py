class CourseSelectionException(Exception):
    pass


class ProfessorAlreadyAssignedException(CourseSelectionException):
    pass


class CourseAlreadySelectedException(CourseSelectionException):
    pass


class CourseNotSelectedException(CourseSelectionException):
    pass


class CourseFullException(CourseSelectionException):
    pass


class InvalidDataExceptions(CourseSelectionException):
    pass


class StudentNotFoundException(CourseSelectionException):
    pass


class ProfessorNotFoundException(CourseSelectionException):
    pass


class CourseNotFoundException(CourseSelectionException):
    pass
