class MathOperations:
    def add(self, *args):
        total = 0
        for num in args:
            total += num
        return total

obj = MathOperations()
print("Addition of:")
print("2 numbers:", obj.add(10, 20))
print("3 numbers:", obj.add(10, 20, 30))
print("5 numbers:", obj.add(1, 2, 3, 4, 5))
