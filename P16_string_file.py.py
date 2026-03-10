# list of strings
lines = ["Apple\n", "Banana\n", "Mango\n", "Orange\n"]

# write list to file
with open("fruits.txt", "w") as f:
    f.writelines(lines)

# read the file
with open("fruits.txt", "r") as f:
    content = f.readlines()

# print content
for line in content:
    print(line.strip())