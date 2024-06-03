from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = h
        self.wigth = w
    
    def area(self):
        return self.height * self.wigth
    
    def perimeter(self):
        return 2 * (self.height +  self.wigth)

class Triangle(Shape):
    def __init__(self, h, b):
        self.height = h
        self.base = b

    def area(self):
        return 0.5 * self.height * self.base
    
    def perimeter(self):
        return 3 * self.base

class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 2 * math.pi * self.radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class RegularHexagon(Shape):
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return (3 * math.sqrt(3) * self.radius ** 2) / 2
    
    def perimeter(self):
        return 6 * self.radius

def main():
    h_r = float(input("원하는 세로 길이를 적어주세요(직사각형): "))
    w = float(input("원하는 가로 길이를 적어주세요(직사각형): "))
    h_t = float(input("원하는 높이를 말해주세요(삼각형): "))
    b = float(input("원하는 밑변의 길이를 말해주세요(삼각형): "))
    r_c = float(input("원하는 반지름의 길이를 말해주세요(원형): "))
    r_r_h = float(input("원하는 변의 길이를 말해주세요(육각형): "))
    shapes = []
    shapes.append(Rectangle(h_r, w))
    shapes.append(Triangle(h_t, b))
    shapes.append(Circle(r_c))
    shapes.append(RegularHexagon(r_r_h))


    for shape in shapes:
        print(shape)
        print("넓이:", shape.area())
        print("둘레",shape.perimeter())

if __name__ == "__main__":
    main()