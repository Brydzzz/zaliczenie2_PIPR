class ValuesOutOfRange(Exception):
    def __init__(self):
        super().__init__("Values are out of range")


class IncorrectCornerCoordinates(Exception):
    def __init__(self):
        super().__init__("Corner coordinates are incorrect")


class BoundingBox:
    def __init__(
        self,
        left_down_corner: tuple[int, int],
        right_up_corner: tuple[int, int],
    ):
        self._left_down_corner = left_down_corner
        self._right_up_corner = right_up_corner
        if not self.check_if_value_in_range():
            raise ValuesOutOfRange
        if not self.check_if_corners_possible():
            raise IncorrectCornerCoordinates

    @property
    def left_down_corner(self):
        return self._left_down_corner

    @property
    def right_up_corner(self):
        return self._right_up_corner

    def check_if_value_in_range(self):
        max_value = 1024
        min_value = 0
        x1, y1 = self.left_down_corner
        x2, y2 = self.right_up_corner
        coordinates = (x1, y1, x2, y2)
        return all(
            min_value <= coordinate <= max_value for coordinate in coordinates
        )

    def check_if_corners_possible(self):
        """
        Checks if right up corner values are bigger than
          left down corner values
        """
        x1, y1 = self.left_down_corner
        x2, y2 = self.right_up_corner
        if_x_correct = x2 > x1
        if_y_correct = y2 > y1
        return if_x_correct and if_y_correct

    def calculate_area(self):
        x1, y1 = self.left_down_corner
        x2, y2 = self.right_up_corner
        x_side = x2 - x1
        y_side = y2 - y1
        area = x_side * y_side
        return area

    def check_if_boxes_intersect(self, other):
        x1_a, y1_a = self.left_down_corner
        x2_a, y2_a = self.right_up_corner
        x1_b, y1_b = other.left_down_corner
        x2_b, y2_b = other.right_up_corner
        intersect_with_left_down = (
            x1_a <= x1_b <= x2_a and y1_a <= y1_b <= y2_a
        )
        intersect_with_right_up = x1_a <= x2_b <= x2_a and y1_a <= y2_b <= y2_a
        return intersect_with_left_down or intersect_with_right_up

    def calculate_intersection(self, other):
        if self.check_if_boxes_intersect(other) is False:
            intersection = 0
        else:
            x1_a, y1_a = self.left_down_corner
            x2_a, y2_a = self.right_up_corner
            x1_b, y1_b = other.left_down_corner
            x2_b, y2_b = other.right_up_corner
            x_left_down = max(x1_a, x1_b)
            y_left_down = max(y1_a, y1_b)
            x_right_up = min(x2_a, x2_b)
            y_right_up = min(y2_a, y2_b)
            x_side = x_right_up - x_left_down
            y_side = y_right_up - y_left_down
            intersection = x_side * y_side
        return intersection

    def calculate_union(self, other):
        first_area = self.calculate_area()
        second_area = other.calculate_area()
        intersection_area = self.calculate_intersection(other)
        union = first_area + second_area - intersection_area
        return union

    def calculate_intersection_over_union(self, other):
        intersection = self.calculate_intersection(other)
        union = self.calculate_union(other)
        return intersection / union

    def calculate_f1_score(self, other):
        intersection = self.calculate_intersection(other)
        first_area = self.calculate_area()
        second_area = other.calculate_area()
        return 2 * intersection / (first_area + second_area)

    def __str__(self):
        x1, y1 = self.left_down_corner
        x2, y2 = self.right_up_corner
        return (
            f"lewy dolny wierzchołek x:{x1} y:{y1}, "
            f"prawy dolny wierzchołek x:{x2} y:{y1}, "
            f"lewy górny wierzchołek x:{x1} y:{y2}, "
            f"prawy górny wierzchołek x:{x2} y:{y2}"
        )
