from src.Figure import Figure


class Square(Figure):
    name = 'Square'

    def __init__(self, side_length):
        self.side_length = side_length

    def area(self) -> float:
        return self.side_length * self.side_length

    def perimeter(self) -> float:
        return (self.side_length + self.side_length) * 2

