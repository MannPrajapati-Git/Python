# project : Personal Expense Tracker

import datetime

# Global list to store expenses
expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount spent (₹): "))
        category = input("Enter category (Food, Travel, Shopping, etc.): ").capitalize()
        note = input("Add a note (optional): ")
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

        expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": date
        }

        expenses.append(expense)
        print(" Expense added successfully!\n")

    except ValueError:
        print(" Invalid amount! Please enter a number.\n")

def view_expenses():
    if not expenses:
        print(" No expenses added yet!\n")
        return

    print("\n All Expenses:")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. ₹{exp['amount']} | {exp['category']} | {exp['note']} | {exp['date']}")
    print()

def total_spent():
    total = sum(exp["amount"] for exp in expenses)
    print(f" Total Spent: ₹{total:.2f}\n")

def filter_by_category():
    if not expenses:
        print(" No expenses added yet!\n")
        return

    category = input("Enter category to filter: ").capitalize()
    filtered = [exp for exp in expenses if exp["category"] == category]

    if not filtered:
        print(f" No expenses found in category '{category}'\n")
    else:
        print(f"\n Expenses in '{category}':")
        for idx, exp in enumerate(filtered, start=1):
            print(f"{idx}. ₹{exp['amount']} | {exp['note']} | {exp['date']}")
        print()

def expense_tracker():
    print(" Welcome to Personal Expense Tracker\n")

    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Filter by Category")
        print("5. Exit\n")

        choice = input(" Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_spent()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            print(" Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the app
expense_tracker()
