import pytest

from src.Square import Square


@pytest.mark.square
def test_area_triangle():
    square = Square(13)
    area_square = square.area()
    assert area_square == 169.0


@pytest.mark.square
def test_perimeter():
    square = Square(13)
    square_area = square.perimeter()
    assert square_area == 52
