import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_student():
    student = chall.Student("John Doe", [90, 80, 85])

    assert student.average() == 85.0, "The average of the grades should be 85.0."

    student.add_grade(100)
    assert student.average() == 88.75, "After adding a grade of 100, the average should be 88.75."

    student_no_grades = chall.Student("Jane Doe", [])
    assert student_no_grades.average() == 0.0, "If the student has no grades, the average should be 0.0."
