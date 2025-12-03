
def getList(size: int):
    return [input("Enter item: ") for _ in range(0, size)]

def getCount(item,l1):
    ctr=len([x for x in l1 if x==item])
    return [item,ctr]

def getFreq(l1):
    freq=[]
    seenitems=[]
    for item in l1:
        if item not in seenitems:
            seenitems.append(item)
            freq.append(getCount(item, l1))
    return freq

def printFreq(freq):
    for item in freq:
        print(f"{item[0]} : {item[1]}")

size=int(input("Enter size: "))
l1=getList(size)
freq=getFreq(l1)
printFreq(freq)
