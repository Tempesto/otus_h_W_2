import pytest

from src.Triangle import Triangle


@pytest.mark.triangle
def test_area_triangle():
    triangle = Triangle(13, 14, 15)
    area_triangle = triangle.area()
    assert area_triangle == 84.0


@pytest.mark.triangle
def test_perimeter():
    triangle = Triangle(13, 14, 15)
    triangle_area = triangle.perimeter()
    assert triangle_area == 42
