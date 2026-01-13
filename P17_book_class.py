
class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = float(price)

    def display(self):
        print(f"{self.name}\t{self.author}\t{self.price}")


size=int(input("Enter count: "))
print(f"Enter {size} books: ")
books=[]
for i in range (size):
    name=input("Name: ")
    author=input("Author: ")
    price=input("Price: ")
    books.append(Book(name, author, price))

print("All Books:")
print("Name\tAuth\tPrice")
for i in range(size):
    books[i].display()

