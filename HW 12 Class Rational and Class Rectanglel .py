
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

print("_"*11)


# 2. Створіть клас «Правильна дроба» та реалізуйте методи порівняння, додавання, віднімання та множення для екземплярів цього класу.

import math

class Rational:

    def __init__(self, a: int, b: int):
        if not isinstance(a, int):
            raise TypeError('Wrong number entered')
        if not isinstance(b, int):
            raise TypeError('Wrong number entered')
        if not b:
            raise ZeroDivisionError()

        self.__a = a
        self.__b = b

    def __add__(self, other):
        if isinstance(self, int):
            other = Rational(self, 1)
        if isinstance(other, int):
            other = Rational(other, 1)
        a = math.lcm(self.__b, other.__b) #Let's use the lcm() function, which returns the least common multiple of the given integer arguments.
        b = (a//self.__b*self.__a)+(a//other.__b*other.__a)
        return Rational(b, a)

    def __radd__(self, other):
        if isinstance(self, int):
            other = Rational(self, 1)
        if isinstance(other, int):
            other = Rational(other, 1)
        a = math.lcm(self.__b, other.__b)
        b = (a//self.__b*self.__a)+(a//other.__b*other.__a)
        return Rational(b, a)

    def __sub__(self, other):
        if isinstance(self, int):
            other = Rational(self, 1)
        if isinstance(other, int):
            other = Rational(other, 1)
        a = math.lcm(self.__b, other.__b)
        b = (a // self.__b * self.__a) - (a // other.__b * other.__a)
        return Rational(b, a)

    def __rsub__(self, other):
        if isinstance(self, int):
            other = Rational(self, 1)
        if isinstance(other, int):
            other = Rational(other, 1)
        a = math.lcm(self.__b, other.__b)
        b = (a // self.__b * self.__a) - (a // other.__b * other.__a)
        return Rational(b, a)

    def __truediv__(self, other):
        if isinstance(self, int):
            other = Rational(self, 1)
        if isinstance(other, int):
            other = Rational(other, 1)
        gcd_1=math.gcd(self.__a, other.__a)
        gcd_2=math.gcd(self.__b,other.__b)
        a=(self.__a//gcd_1)*(other.__b//gcd_2)
        b=(self.__b//gcd_2)*(other.__a//gcd_1)
        return Rational(a, b)

    def __rtruediv__(self, other):
        if isinstance(self, int):
            other = Rational(self, 1)
        if isinstance(other, int):
            other = Rational(other, 1)
        gcd_1=math.gcd(self.__a, other.__a)
        gcd_2=math.gcd(self.__b,other.__b)
        a=(self.__a//gcd_1)*(other.__b//gcd_2)
        b=(self.__b//gcd_2)*(other.__a//gcd_1)
        return Rational(a, b)

    def __mul__(self, other):
        if isinstance(self, int):
            other = Rational(self, 1)
        if isinstance(other, int):
            other = Rational(other, 1)
        gcd_1 = math.gcd(self.__a, other.__b)
        gcd_2 = math.gcd(self.__b, other.__a)
        a = (self.__a // gcd_1) * (other.__a // gcd_2)
        b = (self.__b // gcd_2) * (other.__b // gcd_1)
        return Rational(a, b)

    def __rmul__(self, other):
        if isinstance(self, int):
            other = Rational(self, 1)
        if isinstance(other, int):
            other = Rational(other, 1)
        gcd_1 = math.gcd(self.__a, other.__b)
        gcd_2 = math.gcd(self.__b, other.__a)
        a = (self.__a // gcd_1) * (other.__a // gcd_2)
        b = (self.__b // gcd_2) * (other.__b // gcd_1)
        return Rational(a, b)


#
    def __str__(self):
        sign = '' if self.__a * self.__b > 0 else '-'
        a, b = abs(self.__a), abs(self.__b)
        k = math.gcd(a, b)
        a //= k
        b //= k

        if a == b:
            return f'{sign}1'
        if b == 1:
            return f'{sign}{a}'
        if a > b:
            return f'{sign}{a // b} {a - a // b * b} / {b}'
        return f'{sign}{a} / {b}'
#
#
decimal = Rational(-4,5)
decimal_2 = Rational(-3,4)

print(decimal)
print(decimal_2)


print(decimal+decimal_2)
print(decimal-decimal_2)
print(decimal*decimal_2)
print(decimal/decimal_2)