from src.Figure import Figure

name = 'Rectangle'


class Rectangle(Figure):
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def area(self) -> float:
        return self.sideA * self.sideB

    def perimeter(self) -> float:
        return (self.sideA + self.sideB) * 2
