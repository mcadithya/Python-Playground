

class Singers():

    def __init__(self,name,dob,industry,genre,no_of_songs):

        self.name = name

        self.dob = dob

        self.industry = industry

        self.genre = genre

        self.no_of_songs = no_of_songs

    def display_singer(self):

        print(f"name:{self.name}, date of birth:{self.dob}, industry: {self.industry}, genre : {self.genre}, no of songs : {self.no_of_songs} ")


chithra = Singers("K S Chithra","27 July 1963","Mollywood","playback singer", 500 )

chithra.display_singer()