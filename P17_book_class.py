class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Price: ₹{self.price}")


# Creating book objects
b1 = Book("Python Basics", "Guido", 2020, 450)
b2 = Book("Data Science", "Jake", 2022, 650)

b1.display()
b2.display()
