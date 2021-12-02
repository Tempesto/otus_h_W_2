import pytest

from src.Rectangle import Rectangle


@pytest.mark.rectangle
def test_area_triangle():
    rectangle = Rectangle(13, 14)
    area_rectangle = rectangle.area()
    assert area_rectangle == 182.0


@pytest.mark.rectangle
def test_perimeter():
    rectangle = Rectangle(13, 14)
    rectangle_area = rectangle.perimeter()
    assert rectangle_area == 54
