class InsufficientFundsError(Exception):
    pass

balance = 1000

try:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Updated Balance:", balance)

    elif choice == 3:
        amount = float(input("Enter withdraw amount: "))
        if amount > balance:
            raise InsufficientFundsError("Not enough balance")
        balance -= amount
        print("Updated Balance:", balance)

    else:
        print("Invalid choice")

except ValueError:
    print("Invalid input. Enter numbers only.")

except InsufficientFundsError as e:
    print(e)