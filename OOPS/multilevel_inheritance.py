class GrandFather:

    name: str
    age: int

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def have_land(self):

        print(f'{self.name} owing 1 acre land')

class Father(GrandFather):

    def __init__(self, name, age, profession):

        super().__init__(name, age)

        self.profession = profession

    def have_car(self):

        print(f'{self.name} owning B6')


class Daughter(Father):

    def __init__(self, name, age, profession, marital_status):

        super().__init__(name, age, profession)

        self.marital_status = marital_status

    def have_scooter(self):

        print(f'{self.name} owning Activa')

geeta = Daughter('Geetha', 24, 'software developer', 'single')

geeta.have_land()    #  Inherited from GrandFather

geeta.have_car()     #  Inherited from Father

geeta.have_scooter() #  Defined in Daughter