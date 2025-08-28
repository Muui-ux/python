# Assignment 1
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Inherited class (Inheritance + Encapsulation)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        # Call the parent constructor
        super().__init__(brand, model, storage)
        self.gpu = gpu

    # Overriding (Polymorphism example)
    def info(self):
        print(f"{self.brand} {self.model} (Gaming Edition) - {self.storage}GB, GPU: {self.gpu}")
    
    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} smoothly with {self.gpu} GPU!")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S22", 128)
phone2 = GamingPhone("Asus", "ROG 6", 256, "Adreno 730")

# Using methods
phone1.info()
phone1.call("0723456789")

phone2.info()
phone2.play_game("PUBG Mobile")

# Assignment 2
class Vehicle:
    def move(self):
        print("This vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving ")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat()]

# Polymorphism in action
for v in vehicles:
    v.move()
