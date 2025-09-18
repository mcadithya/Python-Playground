#abstarct --- providing essential details to user by hiding implimentation details
# for using abtraction first import abc.py module, abc - abstract base class
#abstarctmethord is decorater
# for decorater starts with @
# inside a class have atleast one abstract method then that class is known as abstract class
# abstract method dont have any method definition (pass)
#cant create object of a abstract method  
# for abstract method access use another method and inherit that methods
# write all method definition inside that child class 



from abc import ABC,abstractmethod

class Polygon(ABC):
  
    def __init__(self,name,no_of_sides):

        self.name = name
        self.no_of_sides = no_of_sides

    @abstractmethod
    def area(self,**kwargs):

        pass

    def perimeter(self,**kwargs):
        
        pass
   

#polygon_obj = Polygon("polygon","not defined")

class Triangle(Polygon):

    def __init__(self,name,no_of_sides):

        super().__init__(name,no_of_sides)

    def area(self,**kwargs):

        base = kwargs.get("base")

        height = kwargs.get("height")

        return 0.5*base*height
    
    def perimeter(self,**kwargs):

        side_a = kwargs.get("side_a")

        side_b = kwargs.get("side_b")

        side_c = kwargs.get("side_c")

        return side_a + side_b + side_c
    


polygon_obj = Triangle("traingle",3)

print(polygon_obj.area(base = 3,height = 4))

print(polygon_obj.perimeter(side_a = 3 , side_b = 4 ,side_c = 5))



        
