# class Artist -- atributes -- artist_name methods -- acting print('artist_name is acting')

class Artist():

    def __init__(self,artist_name):

        self.artist_name = artist_name

    def acting(self):

        print(f"{self.artist_name} is acting")


artist_object= Artist("Raja Ravi Varma")

artist_object.acting()