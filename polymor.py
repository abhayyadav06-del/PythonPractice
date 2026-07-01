class DietPlan:
    def get_breakfast(self):
        pass

class KetaDiet(DietPlan):
    def get_breakfast(self):
            return "Eggs and Avocado,bacon friend."
         
class VeganDiet(DietPlan):
    def get_breakfast(self):
                return "Oatmeal with milk, chia seed"
    
class HighProteinDiet(DietPlan):
    def get_breakfast(self):
            return "Greek yogurt, and a banana"
        
def print_morning_routine(diet_object):
              print(f"Today's breakfast: {diet_object.get_breakfast()}")

my_keto = KetaDiet()
my_vegan = VeganDiet()
my_protein = HighProteinDiet()

print_morning_routine(my_keto)
print_morning_routine(my_vegan)
print_morning_routine(my_protein) 
