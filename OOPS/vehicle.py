class Vechicle():

    def __init__(self,reg_number,mileage):

        self.reg_number=reg_number

        self.mileage=mileage

    def engine_start(self)  :

        print(f'{self.reg_number} having {self.mileage} starts the engine')

    def engine_stop(self):
        
        print (f'{self.reg_number} having {self.mileage} stops the engine')    

class Car (Vechicle):

    def __init__(self, reg_number, mileage,fuel_type):

        super().__init__(reg_number, mileage)

        self.fuel_type=fuel_type

    def apply_break (self):

        print(f'{self.reg_number} of having{self.mileage} of {self.fuel_type}apply breaks')

class Electricvechicle(Car) :


    def __init__(self, reg_number, mileage, fuel_type,battery_type):
        
        super().__init__(reg_number, mileage, fuel_type) 

        self.battery_type=battery_type  

    def charging_car(self) :

        print(f'{self.reg_number} of having{self.mileage} of {self.fuel_type} and {self.battery_type}apply breaks' )

        print('charging')


nano=Electricvechicle('kl04123','24 mileage' ,'petrol as fuel type','hydrogen as battery type')  

nano.charging_car()


    #    give single print