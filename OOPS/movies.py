class Movies():

    def initialize_movie(self,name, release_year,run_time,director,cast):

        self.name  = name 
        self.year = release_year
        self.run_time = run_time
        self.director = director
        self.cast = cast

    def display_movie(self):

        print(self.name)
        print(self.year)
        print(self.run_time)
        print(self.director)
        print(self.cast)


movie_object = Movies()


movie_object.initialize_movie( "Inception",2010,2.5 ,  "Christopher Nolan",["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"])

movie_object.display_movie()

print()

movie_object.initialize_movie("F1",2025,2.5,"Joseph Kosinski",["Brad Pitt","Kerry Condon"])

movie_object.display_movie()