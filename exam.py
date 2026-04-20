
def inputtest():
    num=input(f"Enter {2+1} Here")
    print(num)

def typetest():
    def val(n):
        print(type(n))
    val(1)
    val(1.1)
    val(1+3j)
    val("hi")
    val(True)

def slicingtest():
    name="python"

    print(name[::2])
    print(name[3:])
    print(name[2::3])
    print(name[3:5])
    print(name[-3:-5:-1])
    print(name[-1::-2])

def listtest():
    a = [5, 10, 15, 20, 25]

    print(a[-2::-1])

def charFreq():
    name=input("String: ")
    freq={}

    for item in name:
        if item not in freq.keys():
            freq[item]=1
        else:
            freq[item]+=1
    
    print(freq)

def fibinacci(end=22):
    fib=1
    prev=0
    print("1")
    while(fib<=end):
        fib,prev=fib+prev,fib
        print(fib)

def lambdatest():
    nums = [1, 2, 3]
    print(list(map(lambda x: x+1, nums)))  

    print(list(map(lambda x: x%2==0, nums)))

def classtest():
    class myclass:
        def __init__(selfany, name, age):
            selfany.name = name
            selfany.age =  age

        def myfun(selfany):
            print("name", selfany.name)
            print("age", selfany .age)
    P1 = myclass("sjc",138)
    P1.myfun()

def fileopentest():
    with open("hello.txt","w") as f:
        f.write("Hello\n")
        f.writelines(list(map(lambda x: str(x)+"\n",[1, 2, 3, 4, 5])))
        f.write("EOF")

    with open("hello.txt", "r") as f:
        data=f.read()
        print(data)

def inherittest():
    class Par():
        def __init__(s, a, b):
            s.a=a
            s.b=b
        
        def addup(s):
            return 20+20
        
        def printpar(s):
            return s.a+s.b
        
    class Child(Par):
        def __init__(s, a, b):
            super().__init__(a, b)

    ch=Child("Hello ", "World!")
    print(f"{ch.printpar()} {ch.addup()}")

def multipleinherittest():
    class A:
        def __init__(self, string):
            print(string)

    class B:
        def __init__(self, n1, n2):
            print(n1+n2)

    class C(A, B):
        def __init__(self):
            print("C")
            B.__init__(self, 1, 2)
    
    c=C()

import re
def regextest():
    p=r"\d"
    s="main maan maaaan massssn woman mango"
    v=re.findall(r"(ma.*?n)", s)
    print(v)

def tryexcepttest():
    class BruhError(Exception):
        def __init__(self, *args):
            print("Nah you dumb")
            super().__init__(*args)
    
    try:
        raise BruhError()
    except BruhError as bruh:
        pass
        # print("Woah")
    finally:
        print("Cool")

tryexcepttest()