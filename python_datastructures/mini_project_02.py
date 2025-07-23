# project : Shopping Cart System

cart = {}

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"{qty} {item}(s) added to cart.")

    elif choice == "2":
        item = input("Enter item name to remove: ")
        if item in cart:
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")

    elif choice == "3":
        if cart:
            print("Items in your cart:")
            for item, qty in cart.items():
                print(f"{item}: {qty}")
        else:
            print("Your cart is empty.")

    elif choice == "4":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")