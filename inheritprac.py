class Animal:

    def __init__(self, name, type, speak):
        self.name = name
        self.type = type
        self.speak = speak

    def display_info(self):
        return f"{self.name} is a {self.type} and it says {self.speak}"

class Pet(Animal):
    pass
my_pet = Pet("Buddy", "Dog", "Woof")
print(my_pet.display_info())
my_pet2 = Pet("Whiskers", "Cat", "Meow")
print(my_pet2.display_info())