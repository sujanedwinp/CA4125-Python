
class Queue:
    def __init__(self):
        self.q=[]

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if self.isEmpty():
            print("Nothing to Dequeue.")
            return None
        return self.q.pop(0)
    
    def showQueue(self):
        if self.isEmpty():
            print("Nothing to Show.")
            return None
        for item in self.q:
            print(item)
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        if self.size()==0:
            return True
        return False

queue=Queue()

while(True):
    print("\nMenu.")
    choice=int(input("1. Enqueue\n2. Dequeue\n3. Show Queue\n4. Size of Queue\n5. Exit\n"))
    if choice==1:
        item=input("Enter Item: ")
        queue.enqueue(item)
    elif choice==2:
        print(f"Item Removed: {queue.dequeue()}")
    elif choice==3:
        print("Queue:")
        queue.showQueue()
    elif choice==4:
        print(f"Size: {queue.size()}")
    elif choice==5:
        print("Exited")
        break
    else:
        print("Try Again")