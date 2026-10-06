# simple class concept
class car:
    def __init__(self, name,year):
        self.name=name
        self.year=year


    def smallcar(self):
        return self.year , self.name

    def common(self):
        print("this is commom to all ",self.name)


class supercar:
    def __init__(self,city,model):
        self.city=city
        self.model=model
    def bigcar(self):
        return self.model

    def common(self):
        print("this is common to all",self.name)

    def slowcar(self):
        return self.city

