
size=int(input("Enter Size: "))
print("Enter Elements")
regno=tuple([input() for _ in range(0, size)])

# 1
print("RegNo:")
[print(x) for x in regno]

# 2
item=input("Enter Reg Number to check: ")

if item in regno:
    print(f"Found at postion {regno.index(item)+1}")
else:
    print("Not Found")

# 3
print(f"{len(regno)} size")