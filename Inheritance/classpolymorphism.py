class Movie :
    def __init__(self,picture,year):
        self.picture=picture
        self.year=year
    def cinema(self):
        print("the name of movies is",self.picture)
    def samemessages(self):
        print("the year of movies",self.year)
class mumbai :
    def __init__(self,place,city):
        self.place =place
        self.city=city
    def  bombay(self):
        print('this is the place',self.place)

    def bombaydinne(self):
        print("this is city which name is ",self.city)

    def samemessages(self):
        print("the year of movies",self.city)

M1=Movie("ddlg",1998)

M1.cinema()

M1.samemessages()
M1.year

samemessages()