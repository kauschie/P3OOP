from .grader import Grader, AssignmentGrader
from .lessons import IntroToPython, Statistics

def start_assignment(self, student, id):
    self.student_graders[student] = AssignmentGrader(
        student, self
    )