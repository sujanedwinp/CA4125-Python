
class Vehicle:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

    def display_info(self):
        print(f"Speed: {self.speed} km/h")
        print(f"Fuel: {self.fuel}")

class Car(Vehicle):
    def car_type(self, type):
        print(f"Car Type: {type}")

class Motorcycle(Vehicle):
    def engine_size(self, cc):
        print(f"CC: {cc}")

class Truck(Vehicle):
    def cargo_capacity(self, capacity):
        print(f"Cargo Capacity: {capacity} tons")

car = Car(120, "Petrol")
car.display_info()
car.car_type("Sedan")

bike = Motorcycle(90, "Petrol")
bike.display_info()
bike.engine_size(300)

truck = Truck(80, "Diesel")
truck.display_info()
truck.cargo_capacity(10)
