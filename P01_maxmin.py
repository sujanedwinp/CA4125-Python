
def getList():
    l1=[]
    while True:
        num=input("Enter number or \"s\" to save list: ")
        if num.isalpha() and num[0]=="s":
            return l1
        else:
            l1.append(float(num))

def minmaxnum(l1: list):
    minv=float('inf')
    maxv=-float('inf')
    for n in l1:
        if n<=minv:
            minv=n
        if n>=maxv:
            maxv=n

    return [min, max]

l1=getList()
[minv, maxv]=minmaxnum(l1)
print(f"list: {l1}\nmin: {minv}\nmax: {maxv}")
