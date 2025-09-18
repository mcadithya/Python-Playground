# parent class---constructor  child class must  have constructor

# call parent class constructor method from child constructor method 

class Father:

    def __init__(self,name,age):
        
        self.name=name
        
        self.age=age

    def singing(self):

        print(f'{self.name} sings well',self.age)  

    def dance(self):

        print(f'{self.name} dance well') 

father=Father('alex',77)  

father.singing()

father.dance()


class Son(Father)  :    #inherit

    def __init__(self,name,age,profession) :  #class attributes from parent    attributes from parent works here

        super().__init__(name,age)

        self.profession = profession   #initialise its own attribute

    def details(self):

         print(self.profession)

son=Son('prince',25,'doctor')

son.singing()

son.dance()

son.details()