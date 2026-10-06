# simple class concept
class car:
    def __init__(self, name,year):
        self.name=name
        self.year=year


    def smallcar(self):
        return self.year , self.name

class supercar:
    def __init__(self,city,model):
        self.city=city
        self.model=model
    def bigcar(self):
        return self.model

    def slowcar(self):
        return self.city

car1= car("maruti800",1992)
car1.smallcar()

csup=supercar("i10","goa")
csup.slowcar()
csup.bigcar()

