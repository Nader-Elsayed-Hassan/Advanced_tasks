# Rectangle class :- 
class Rectangle: 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
    def area(self): 
        return self.width * self.height 
    def perimeter(self): 
        return 2 * (self.width + self.height) 
rect1 = Rectangle(width=10, height=5) 
print(f"Area: {rect1.area()}")  
print(f"Perimeter: {rect1.perimeter()}")



# Vehicle Hierarchy :- 
class Vehicle: 
    def move(self): 
        print("Vehicle is moving") 
class Car(Vehicle): 
    def move(self): 
        print("Car is driving") 
class Bike(Vehicle): 
    def move(self): 
        print("Bike is cycling") 
vehicles = [Vehicle(), Car(), Bike()] 
for v in vehicles: 
    v.move() 
    
    
    
# Vector class with Operator overloading :- 
class Vector:     
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def __str__(self): 
        return f'Vector({self.x}, {self.y})' 
    def __sub__(self, other): 
        new_x = self.x - other.x 
        new_y = self.y - other.y 
        return Vector(new_x, new_y) 
    def __mul__(self, other): 
        return (self.x * other.x) + (self.y * other.y) 
v1 = Vector(5, 7) 
v2 = Vector(2, 3) 
v_diff = v1 - v2  
print(f"v1 - v2 (Subtraction): {v_diff}")  
dot_product = v1 * v2 
print(f"v1 * v2 (Dot Product): {dot_product}")



# Shape Polymorphism Function :- 
import math 
class Shape: 
    def area(self): 
        raise NotImplementedError("Subclass must implement abstract method 'area'")
class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 
    def area(self): 
        return math.pi * self.radius**2 
class Rectangle(Shape): 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
    def area(self): 
        return self.width * self.height 
def print_shape_area(shape): 
    print(f"The area is: {shape.area():.2f}") 
s_generic = Shape() 
c1 = Circle(radius=3) 
r1 = Rectangle(width=4, height=5) 
print_shape_area(c1) 
print_shape_area(r1)