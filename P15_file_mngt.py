# create and write to file

with open("sample.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python File Handling\n")

# append dat
with open("sample.txt", "a") as f:
    f.write("This line is appended\n")

# use seek to move cursor and read
with open("sample.txt", "r") as f:
    f.seek(0)        # move cursor to beginning
    data = f.read()
    print(data)