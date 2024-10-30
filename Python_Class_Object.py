class Laptop:
    def __init__(self, brand, release_year, color,RAM):
        self.laptop_brand = brand
        self.laptop_release_year = release_year
        self.laptop_color = color
        self.laptop_RAM = RAM
    def information(self):
        return f"{self.laptop_color} Laptop {self.laptop_brand} release in {self.laptop_release_year} with {self.laptop_RAM} RAM"
    
class GamingLaptop(Laptop):
    def __init__(self, brand, release_year, color, RAM, VGA):
        super().__init__(brand, release_year, color, RAM)
        self.laptop_VGA = VGA

laptop_1 = Laptop("Dell", 2021, "Grey", 8)

print(Laptop)
print(laptop_1)
print(laptop_1.laptop_brand)
print(laptop_1.information())