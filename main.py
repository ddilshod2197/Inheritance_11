# 11. Bog‘dorchilik rejasi
class Plant:
    def __init__(self, name, water_needed):
        self.name = name           
        self.water_needed = water_needed  

    def watering_plan(self):
        """Kunlik sug'orish miqdori"""
        return self.water_needed

    def __str__(self):
        return f"{self.name:12} | {self.water_needed:4} litr"



class Flower(Plant):
    def __str__(self):
        return f"🌸 {self.name:10} → {self.water_needed} litr suv"


class Tree(Plant):
    def __str__(self):
        return f"🌳 {self.name:10} → {self.water_needed} litr suv"



def show_watering_plan(plants):
    print("\n" + "═" * 50)
    print("   BOG‘DORCHILIK — SUG‘ORISH REJASI   ".center(50))
    print("═" * 50)
    print("O‘simlik         Sug‘orish miqdori")
    print("─" * 50)

    total_water = 0

    for plant in plants:
        print(plant)
        total_water += plant.watering_plan()

    print("─" * 50)
    print(f"Kunlik jami suv:          {total_water:6} litr")
    print("═" * 50 + "\n")


bog = [
    Flower("Atirgul", 2),
    Flower("Lola", 1),
    Flower("Romashka", 1.5),
    Tree("Olma daraxti", 10),
    Tree("O'rik", 8),
    Tree("Shaftoli", 7),
]

show_watering_plan(bog)

print("\nSizning misolingiz:\n")
misol_bog = [
    Flower("Gul", 2),
    Tree("Daraxt", 5),
]

show_watering_plan(misol_bog)
