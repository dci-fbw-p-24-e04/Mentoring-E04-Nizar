class Circle:
    def area(self,radius):
        print(f"the area of the circle is {3.14*radius*radius}")
        
        
class Rectangle:
    def area(self,width,length):
        print(f"the area of the rectangle is {length*width}")
        
class AreaCalc:  
    def calculate_object_area(self,obj,*args):
        print('calculating the area')
        print('...')
        obj.area(*args)
        
        
calc = AreaCalc()
calc.calculate_object_area(Circle(),5)
calc.calculate_object_area(Rectangle(),7,3)