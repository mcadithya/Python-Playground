# encapsulation  ability methods and attributes hold together
# 

# overreading

# overloading


class Polygon:

    def __init__(self,no_of_sides):

        self.no_of_sides= no_of_sides

    def area(self,**kwargs):

        return None
    
    def perimeter(self,**kwargs):

        return None
    
class Triangle(Polygon):

    def __init__(self, no_of_sides):

        super().__init__(no_of_sides)

    def area(self, **kwargs):

        base=kwargs.get('base')

        height=kwargs.get('height')

        return 0.5*base*height
    
    def perimeter(self, **kwargs):
        
        side_a=kwargs.get('side_a')

        side_b=kwargs.get('side_b')

        side_c=kwargs.get('side_c')

        return side_a+side_b+side_c

triangle_obj=Triangle(3)

print(triangle_obj.area(base=3,height=5))

print(triangle_obj.perimeter(side_a=3,side_b=4,side_c=5))

class Rectangle(Polygon):

    def __init__(self, no_of_sides):

        super().__init__(no_of_sides)

    def area(self,**kwargs):

        length=kwargs.get('length')

        breadth=kwargs.get('breadth')

        return length*breadth
    
    def perimeter(self, **kwargs):
        
        length=kwargs.get('length')

        breadth=kwargs.get('breadth')

        return 2*(length+breadth)
    
rect_obj=Rectangle(2)

print(rect_obj.area(length=3,breadth=4))

print(rect_obj.perimeter(length=3,breadth=4))