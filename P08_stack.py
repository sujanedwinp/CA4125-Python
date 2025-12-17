
class Stack:
    def __init__(self):
        self.st=[]

    def pushStack(self, item):
        self.st.append(item)

    def popStack(self):
        if self.isEmpty():
            print("Nothing to Remove.")
            return None
        return self.st.pop()
    
    def showStack(self):
        if self.isEmpty():
            print("Nothing to Show.")
            return None
        for item in reversed(self.st):
            print(item)
    
    def topItem(self):
        if self.isEmpty():
            print("No Top Item.")
            return None
        return self.st[-1]
    
    def size(self):
        return len(self.st)
    
    def isEmpty(self):
        if self.size()==0:
            return True
        return False

stack=Stack()
stack.pushStack(1)
stack.pushStack("Hello")
stack.pushStack(True)
stack.pushStack(3.14)
stack.showStack()