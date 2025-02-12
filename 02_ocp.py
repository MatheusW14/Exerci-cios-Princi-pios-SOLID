from abc import ABC, abstractmethod


# Classe abstrata para definir a interface das formas
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Classe para representar um retângulo
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Classe para representar um círculo
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


# Classe para calcular a área das formas (sem precisar ser modificada)
class ShapeAreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()


# Exemplo de uso:
rectangle = Rectangle(5, 10)
circle = Circle(7)

calculator = ShapeAreaCalculator()
print(calculator.calculate_area(rectangle))  # Saída: 50
print(calculator.calculate_area(circle))  # Saída: 153.86
