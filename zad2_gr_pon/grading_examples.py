from grading_classes import Grade, GradingType

school_grading = GradingType(
    1, 5, 0.5, {1: "F", 2: "D", 3: "C", 4: "B", 5: "A"}
)
university_grading = GradingType(
    2,
    5,
    1,
    {2: "Fail", 3: "Pass", 4: "Merit", 5: "Distinction"},
)

polish_grading = GradingType(
    1, 6, 0.5, {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6"}
)

grade1 = Grade(3.5, school_grading)
grade2 = Grade(4, university_grading)
grade3 = Grade(2, polish_grading)

print(grade1.value)
print(grade1.grading_type.grade_display_values)
print(grade1.grading_type.interval)
print(grade1 < grade2)
print(grade1 == grade2)
print(grade3 < grade1)
print(grade3 == grade2)
