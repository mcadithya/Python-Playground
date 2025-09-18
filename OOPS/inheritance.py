# to transfer methods and attributes of one class into another class

# the process in which one class acquires methods and attributes of another class 

# parent class or super class----from where its taken

# child class or sub class-------to where its taken(many type)


# single inheritance---only single parent class class b inheritance from a

# multilevel inheritance----b acquires from a and c acquires from b  

# multiple inheritance------- twomparent a and b so on c inherit from both a and b 

class ArchaFather:
    # def __init__(self,name):

    #     self.name = name

    def driving(self,name):

        print(f'{name} is driving i20')

father=ArchaFather()  

father.driving('name')

# inheritance


#for inheritance open bracket and give the class name which we need to transfer
class Archa(ArchaFather):

    pass

archa=Archa()

archa.driving('archa')