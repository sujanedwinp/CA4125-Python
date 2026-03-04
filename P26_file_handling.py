filename = input("Enter file name: ")

try:
    file = open(filename, "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("File not found")