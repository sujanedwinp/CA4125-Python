class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = float(price)

    def display(self):
        print(f"{self.make}\t{self.model}\t{self.year}\t{self.price}")


size=int(input("Enter count: "))
print(f"Enter {size} cars:")
cars=[]
for i in range (size):
    make=input("Make: ")
    model=input("Model: ")
    year=input("Year: ")
    price=input("Price: ")
    cars.append(Car(make, model, year, price))

gprice=int(input("Enter price: "))

print(f"Cars above {gprice}")
print("Make\tModel\tYear\tPrice")
[print(car.display()) for car in cars if car.price > gprice]

