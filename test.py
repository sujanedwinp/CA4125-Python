class MyClass:
    def __init__(mine, a):
        mine.a=a
        pass

    def print(mine, a):
        print(a)
        print(mine.a)

obj=MyClass(10)
obj.print(True)
print(obj.a)