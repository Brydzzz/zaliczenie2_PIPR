from bounding_box import (
    BoundingBox,
    ValuesOutOfRange,
    IncorrectCornerCoordinates,
)
import pytest


def test_create_bounding_box_typical():
    boundingbox = BoundingBox((0, 8), (12, 9))
    assert boundingbox.left_down_corner == (0, 8)
    assert boundingbox.right_up_corner == (12, 9)


def test_create_bounding_box_out_of_range():
    with pytest.raises(ValuesOutOfRange):
        BoundingBox((1025, 8), (12, -9))


def test_create_bounding_box_incorrect_coordinates():
    with pytest.raises(IncorrectCornerCoordinates):
        BoundingBox((1024, 8), (1, 3))


def test_calculate_area():
    boundingbox = BoundingBox((0, 0), (10, 10))
    area = boundingbox.calculate_area()
    assert area == 100


def test_calulate_intersection():
    boundingbox1 = BoundingBox((0, 0), (10, 10))
    boundingbox2 = BoundingBox((0, 1), (10, 11))
    intersection = boundingbox1.calculate_intersection(boundingbox2)
    assert intersection == 90


def test_calulate_intersection_same_x():
    boundingbox1 = BoundingBox((3, 8), (5, 10))
    boundingbox2 = BoundingBox((4, 9), (7, 13))
    intersection = boundingbox1.calculate_intersection(boundingbox2)
    assert intersection == 1


def test_calulate_intersection_boxes_dont_intersect():
    boundingbox1 = BoundingBox((0, 0), (10, 10))
    boundingbox2 = BoundingBox((100, 300), (800, 1000))
    intersection = boundingbox1.calculate_intersection(boundingbox2)
    assert intersection == 0


def test_calculate_union():
    boundingbox1 = BoundingBox((0, 0), (10, 10))
    boundingbox2 = BoundingBox((0, 1), (10, 11))
    union = boundingbox1.calculate_union(boundingbox2)
    assert union == 110


def test_calculate_intersection_over_union():
    boundingbox1 = BoundingBox((0, 0), (10, 10))
    boundingbox2 = BoundingBox((0, 1), (10, 11))
    iou = boundingbox1.calculate_intersection_over_union(boundingbox2)
    assert iou == pytest.approx(0.8181818182)


def test_calculate_f1_score():
    boundingbox1 = BoundingBox((0, 0), (10, 10))
    boundingbox2 = BoundingBox((0, 1), (10, 11))
    iou = boundingbox1.calculate_f1_score(boundingbox2)
    assert iou == 0.90
