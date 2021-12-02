import pytest

from src.Circle import Circle


@pytest.mark.circle
def test_area_triangle():
    circle = Circle(13)
    area_circle = circle.area()
    assert area_circle == 530.929158456675


@pytest.mark.circle
def test_perimeter():
    circle = Circle(13)
    circle_area = circle.perimeter()
    assert circle_area == 81.68140899333463
