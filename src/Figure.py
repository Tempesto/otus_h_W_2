from abc import ABC, abstractmethod

name = "Figure"


class Figure(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def add_area(self, other: 'Figure') -> float:
        return self.area() + other.area()
