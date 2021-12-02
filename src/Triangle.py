import math

from src.Figure import Figure


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, a: float, b: float, c: float):
        if a > b + c or b > a + c or c > a + b:
            raise ValueError(
                'Сторона треугольника не может быть больше суммы двух'
                ' других сторон'
            )
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2

        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def perimeter(self) -> float:

        return int(self.a + self.b + self.c)
