class Fruits():

    def __init__(self,name,colour,taste,shape):

        self.name = name

        self.colour = colour

        self.taste  = taste

        self.shape =shape

    def display_fruits(self):

        print(f"name: {self.name}, colour: {self.colour}, taste : {self.taste}, shape : {self.shape}")


apple = Fruits("Apple","red","sweet","round")

apple.display_fruits()



# class Fruits():

#     def __init__(self,*arg):

#         self.name , self.colour, self.taste, self.shape = arg

#     def display_fruits(self):

#         print(f"name: {self.name}, colour: {self.colour}, taste : {self.taste}, shape : {self.shape}")


# apple = Fruits("Apple","red","sweet","round")

# apple.display_fruits()