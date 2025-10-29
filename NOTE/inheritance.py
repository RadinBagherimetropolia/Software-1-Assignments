#class 1
class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def print_info(self):
        print(f"{self.name} is in {self.species}")

    def sound(self):
        print(f"{self.name} says sound.....")


#class2
class Zoo:


    def __init__(self):
        self.count = 0
        self.animal = []

    def add_animal(self, animal):
        self.animal.append(animal)

    def display(self):
        for i in self.animal:
            print(i)

    def sounds(self):
        for i in self.animal:
            print(i.sound())



class Lion(Animals):
    def __init__(self, name, sound = "rrrrooowww" , species = "Lion"):
        super().__init__(name, species)
        self.sound = sound
        super().print_info()
        print(f"the sound is {self.sound}")


class Elephant(Animals):
    def __init__(self, name, sound = "phhhhhhhh"  , species = "Elephant"):
        super().__init__(name, species)
        self.sound = sound
        super().print_info()
        print(f"the sound is {self.sound}")

class Snake(Animals):
    def __init__(self, name, sound = "ssssss" , species = "Snake"):
        super().__init__(name, species)
        self.sound = sound
        super().print_info()
        print(f"the sound is {self.sound}")





#main program
an1 = Lion("cat", "meow")
an2 = Elephant("mammoth" , "pphhhh")
an3 = Snake("cobra" , "sss" )
my_zoo = Zoo()




my_zoo.add_animal(an1)
my_zoo.add_animal(an2)
my_zoo.add_animal(an3)
