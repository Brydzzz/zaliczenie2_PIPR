from grading_classes import GradingType, Grade


def test_create_grading_type():
    polish_grades = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6"}
    polish_grading = GradingType(1, 6, 0.5, polish_grades)
    assert polish_grading.min_grade == 1
    assert polish_grading.max_grade == 6
    assert polish_grading.interval == 0.5
    assert polish_grading.grade_display_values == polish_grades


def test_create_grade():
    polish_grades = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6"}
    polish_grading = GradingType(1, 6, 0.5, polish_grades)
    grade = Grade(4, polish_grading)
    assert grade.value == 4
    assert grade.grading_type == polish_grading


def test_grade_comparison():
    school_grading = GradingType(
        2,
        5,
        0.5,
        {2: "D", 3: "C", 4: "B", 5: "A"},
    )
    university_grading = GradingType(
        2,
        5,
        1,
        {2: "Fail", 3: "Pass", 4: "Merit", 5: "Distinction"},
    )
    grade1 = Grade(3.5, school_grading)
    grade2 = Grade(4, university_grading)
    assert (grade1 < grade2) is False
    assert (grade1 == grade2) is False
