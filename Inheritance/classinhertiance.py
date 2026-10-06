# class Animal:
#     def __init__(self,name,types):
#         self.name=name
#         self.types=types
#     def smallanimal(self):
#         print("the name of smallanimal",self.name)
#     def biganimal(self):
#         print("the biganimal type",self.types)
# class Dog(Animal):
#     def __init__(self,voice,place):
#         self.voice=voice
#         self.place=place
#     super().__(name,types,voice,place)
#     def Cat(self):
#         print("this is voice of cat",self.voice)
#     def Parrot(self):
#         print("this is bird which goes from her to there",self.place)
#
# class Monkey(Animal):
#     def __init__(self,jungel,pet ):
#         super().__init__(name,types,jungel,pet )
#         self.jungel=jungel
#         self.pet=pet
#
#     def Tiger(self):
#         print("this is big animal",self.jungel)
#         print("the name of animal is ",self.name)
#
#     def Lion(self):
#         print("this is pet animal ",self.pet)
#         print(" it has many type on of them ",self.types)
#
# A2=Animal("Lepord","carnivorious")
# A2.smallanimal()
#         # A2 is instance and slf is attribbute,def mumbai is method


class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  # This method will be overridden by subclasses


class Dog(Animal):
    def __init__(self, breed):
        super().__init__('Dog')  # Call superclass constructor
        self.breed = breed

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, color):
        super().__init__('Cat')  # Call superclass constructor
        self.color = color

    def make_sound(self):
        return "Meow!"


# Creating instances of subclasses
dog = Dog('Labrador')
cat = Cat('White')

# Accessing attributes inherited from superclass
print(dog.species)  # Output: Dog
print(cat.species)  # Output: Cat

# Calling methods inherited from superclass
print(dog.make_sound())  # Output: Woof!a
print(cat.make_sound())  # Output: Meow!


