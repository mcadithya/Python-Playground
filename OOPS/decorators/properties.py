class Calculations:

    def __init__ (self,num_1,num_2):
        self.num_1=num_1

        self.num_2=num_2

    @property                      #--------using to treat as attribute
    def sum(self):

        return self.num_1 +self.num_2
    
    @property
    def product(self):

        return self.num_1*self.num_2
    

    
    
objt= Calculations(15,20)

print(objt.num_1)

# can treat method as attribute for that use decorator property but there should only self in it

print(objt.sum) 

print(objt.product)



