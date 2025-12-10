
PhoneBook={}

def add(name, phno):
    PhoneBook[name]=phno

def search(name):
    if name in PhoneBook.keys():
        return f"Phno: {PhoneBook[name]}"
    else:
        return f"Not Found"
    
def delete(name):
    if name in PhoneBook.keys():
        del PhoneBook[name]
    else:
        print("Not Found")

while(True):
    print("Menu.")
    choice=int(input("1. Add Contact\n2. Search Contact(name)\n3. Remove Contact\n4. Exit\n"))
    if choice==1:
        name=input("Enter Name: ")
        phno=input("Enter Phno: ")
        add(name, phno)
    elif choice==2:
        name=input("Enter Name: ")
        print(search(name))
    elif choice==3:
        name=input("Enter Name: ")
        delete(name)
    elif choice==4:
        print("Exited.")
        break
    else:
        print("Try Again")
    