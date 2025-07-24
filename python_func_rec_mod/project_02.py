# project : ATM simulation 
# uses functions + conditional llogic


balance = 10000

def check_balance():
    print("Your current balance is ₹", balance)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn. New balance: ₹{balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"₹{amount} deposited. New balance: ₹{balance}")

def atm():
    print("Welcome to Simple ATM")
    while True:
        print("\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = int(input("Enter amount to withdraw: "))
            withdraw(amt)
        elif choice == '3':
            amt = int(input("Enter amount to deposit: "))
            deposit(amt)
        elif choice == '4':
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice!")

atm()
