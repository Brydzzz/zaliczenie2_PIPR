class GradingType:
    def __init__(
        self, min_grade, max_grade, interval, grade_display_values: dict
    ):
        self._min_grade = min_grade
        self._max_grade = max_grade
        self._interval = interval
        self._grade_display_values = grade_display_values

    @property
    def min_grade(self):
        return self._min_grade

    @property
    def max_grade(self):
        return self._max_grade

    @property
    def interval(self):
        return self._interval

    @property
    def grade_display_values(self):
        return self._grade_display_values


class Grade:
    def __init__(self, value, grading_type: GradingType):
        self._value = value

        self._grading_type = grading_type

    @property
    def value(self):
        return self._value

    @property
    def grading_type(self):
        return self._grading_type

    def normalized_value(self):
        return (
            self.value - self.grading_type.min_grade
        ) / self.grading_type.interval

    def __lt__(self, other):
        return self.normalized_value() < other.normalized_value()

    def __eq__(self, other):
        return self.normalized_value() == other.normalized_value()
