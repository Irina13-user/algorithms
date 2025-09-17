class Point:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.name} ({self.x}; {self.y})"


class Vector:
    def __init__(self, point1, point2):
        self.start = point1
        self.end = point2
        self.x = point2.x - point1.x
        self.y = point2.y - point1.y

    def __repr__(self):
        return f"{self.start.name}{self.end.name} ({self.x}; {self.y})"

    def __add__(self, other):
        X = Point("X")
        Y = Point("Y", self.x + other.x, self.y + other.y)
        return Vector(X, Y)

    def increasing(self, increase1, increase2):
        self.increase1 = increase1
        self.increase2 = increase2
        self.x = self.x + increase1
        self.y = self.y + increase2


    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** .5


A = Point("A", 1, 2)
B = Point("B", 4, 6)
C = Point("C")
v1 = Vector(A, B)
v2 = Vector(A, C)
increase1 = 10
increase2 = 20
print(v1)
print(v1.get_length())
print(v2)
print(v2.get_length())
v3 = v1 + v2
v2 += v3
print(v2)
print(v1.increasing())