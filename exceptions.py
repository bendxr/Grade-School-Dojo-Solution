class StudentAlreadyAddedException(ValueError):
    """
    Exception raised when a student has already been added to a grade.    
    message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


class GradeOutOfRangeException(ValueError):
    """
    Exception raised when a grade is out of the pre-defined range of allowed grades at the school creation ([1; n])
    message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message
