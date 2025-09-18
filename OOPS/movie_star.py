#  name=str

#  age=int

class Movie_star():
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def acting(self):
        
        print(f"{self.name} acting well" )

    
actor = Movie_star('mamooty',70)

actor.acting()


class Dq(Movie_star):

    def __init__(self,name,age,hobby,profession):

        super().__init__(name,age)

        self.hobby=hobby

        self.profession=profession

    def details(self):

        print(self.hobby,self.profession)    
        

dq=Dq('dq',30,'dance','actor')

dq.acting()

dq.details()

