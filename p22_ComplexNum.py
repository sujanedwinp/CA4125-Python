class Complex:
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overload + operator
    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    # Overload - operator
    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    # String representation
    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Create objects
c1 = Complex(3, 4)
c2 = Complex(1, 2)

# Perform operations
c3 = c1 + c2
c4 = c1 - c2

print("Addition:", c3)
print("Subtraction:", c4)
