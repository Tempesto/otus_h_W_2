import math

from src.Figure import Figure

name = "Circle"


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
