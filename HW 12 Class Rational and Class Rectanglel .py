
# 1. Створіть клас «Прямокутник», у якого є два поля (ширина і висота). Реалізуйте метод порівняння прямокутників за площею.
# Також реалізуйте методи складання прямокутників (площа сумарного прямокутника повинна дорівнювати сумі площ прямокутників, які ви складаєте).
# Реалізуйте методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).

class Rectangle:

    def __init__(self, width: int | float, length: int | float):
        self.x = width
        self.y = length


    def square(self) -> int | float:
        return self.x * self.y

    def __gt__(self, other):
        return self.square() > other.volume()

    def __lt__(self, other):
        return self.square() < other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.square() + other.square()
        if isinstance(other, int | float):
            return self.square() + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.square() + other
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.square()*other
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
           return self.square() * other

        return NotImplemented


    def __str__(self):
        return f'{self.x} x {self.y}'

x = Rectangle(5, 10)
y = Rectangle(3, 4)

print(x)
print(y)
print(x*9)
print(5*x)
print(x.__mul__(6))

# 2. Створіть клас «Правильна дроба» та реалізуйте методи порівняння, додавання, віднімання та множення для екземплярів цього класу.