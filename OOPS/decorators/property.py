
class Calculation():

    def __init__(self,num_1,num_2):

        self. num_1 = num_1

        self.num_2 = num_2

    @property

    def sum(self):

        return self.num_1 + self.num_2 
    
    @property

    def product(self):

        return self.num_1 * self.num_2

obj = Calculation(15,20)

print(obj.num_1)

print(obj.num_1)

# print(obj.sum())

#print(obj.sum)  ===> cant call like this, if you wnat to treate method ike a attribute then use property decorator. this decorator use only if that method have only self parameter


print(obj.sum)

print(obj.product)

