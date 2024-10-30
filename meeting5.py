class Laptop:
    def __init__(self, brand, release_year, color,RAM):
        self.laptop_brand = brand
        self.laptop_release_year = release_year
        self.laptop_color = color
        self.laptop_RAM = RAM

    # Add the code below
    def information(self):
        return f"{self.laptop_color} Laptop {self.laptop_brand} release in {self.laptop_release_year} with {self.laptop_RAM} RAM"
    
    def coding(self):
        print("Laptop used for coding ....")
        print("RAM usage : 2GB")
        self.laptop_RAM -= 2;
        print("Remaining RAM : " + str(self.laptop_RAM) + " GB")
    
    def office(self):
        print("Laptop used for office ....")
        print("RAM usage : 1GB")
        self.laptop_RAM -= 1;
        print("Remaining RAM : " + str(self.laptop_RAM) + " GB")

class GamingLaptop(Laptop):
    def __init__(self, brand, release_year, color, RAM, VGA):
        super().__init__(brand, release_year, color, RAM)
        self.laptop_VGA = VGA

    def gaming(self):
        print("Laptop used for gaming ....")
        print("Using " + self.laptop_VGA)
        print("My brand is " + self.laptop_brand)
        print("RAM usage : 10GB")
        self.laptop_RAM -= 10;
        print("Remaining RAM : " + str(self.laptop_RAM) + " GB")

laptop_1 = GamingLaptop("Dell", 2021, "Grey", 8, "gsdgfiuw")
laptop_2 = GamingLaptop("Asus", 2022, "Black", 16, "RTX 1650")

print(laptop_1.laptop_brand)
print(laptop_1.information())
# Add the code below
laptop_1.coding()
laptop_1.office()
print(laptop_2.information())
# Add the code below
laptop_2.gaming()
laptop_1.gaming()