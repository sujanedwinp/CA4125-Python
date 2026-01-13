
class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def display(self):
        print(f"Name: {self.name}\tAuthor: {self.author}\tPrice: ₹{self.price}")


size=int(input("Enter count: "))
print(f"Enter {size} books")
books=[]
for i in range (size):
    name=input("Name: ")
    author=input("Author: ")
    price=input("Price: ")
    books.append(Book(name, author, price))

print("All Books:")
for i in range(size):
    books[i].display()

