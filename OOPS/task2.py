# class Director -- atributes -- director_name methods--- directing print('director_name is directing')

class Director():

    def __init__(self,director_name):

        self.director_name = director_name
    
    def directing(self):

        print(f"{self.director_name} is directing")


director_object =  Director("Joseph Kosinski")

director_object.directing()