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
        
class AreaCalc:  
    def calculate_object_area(self,obj,):
        print('calculating the area')
        print('...')
        obj.area()
        
        
calc = AreaCalc()
calc.calculate_object_area(Circle(5))
calc.calculate_object_area(Rectangle(7,3))