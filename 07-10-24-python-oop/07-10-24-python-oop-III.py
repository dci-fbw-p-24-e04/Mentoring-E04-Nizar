from abc import ABC,abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        print(f"the area of the circle is {3.14*self.radius**2}")
        
    def perimeter(self):
        print(f"the perimeter of the circle is {3.14*2*self.radius}")
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print( self.width * self.height)

    def perimeter(self):
        print( 2 * (self.width + self.height))
        
    def volume(self):
        print("2D shapes have no volumes")
        

class Ellipse(Shape):
    def __init__(self,a,b) :
        self.a = a
        self.b = b
        
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def rate(self):
        print("the rate is :",self.a/self.b)
        
circle = Circle(5)
circle.area()
rect = Rectangle(6,7)
rect.volume()
ecl = Ellipse(7,2)
ecl.rate()
#shape = Shape().area() cant do that