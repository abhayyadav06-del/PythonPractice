# Dfine the parent class to hold general data

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand 
        self.year = year
    def display_info(self):
            return f"{self.brand} - {self.year}"

class Car(Vehicle):
    pass
my_car = Car("BMW", 2026)
print(my_car.display_info())