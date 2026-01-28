
class Product:
    def __init__(self, pid, name, price):
        self.pid = f"SAM{pid}"
        self.name = name
        self.price = price

class ElectronicsProduct(Product):
    def __init__(self, pid, name, price, brand):
        super().__init__(pid, name, price)
        self.brand = brand

    def display_details(self):
        print(f"ID: {self.pid}")
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Brand: {self.brand}")

device = ElectronicsProduct(101, "Sam 1", 25000, "Samsung")
device.display_details()
