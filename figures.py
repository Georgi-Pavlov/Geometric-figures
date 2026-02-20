from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        sides = sorted([a, b, c])
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def type_(self):
        sides = sorted([self.a, self.b, self.c])
        if sides[2]**2 == sides[0]**2 + sides[1]**2:
            return "right angle"
        elif len(set(sides)) == 1:
            return "equilateral"
        elif len(set(sides)) == 2:
            return "isosceles"
        else:
            return "standard"

    def area(self):
        s = self.perimeter() / 2
        return f"{sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)):.2f}"
