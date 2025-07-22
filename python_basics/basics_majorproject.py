# combination of all the basics projects 

admin="mann"
password="1234"
print("Welcome to the Basics Projects Interface!")
print("Please log in to access the projects.")
while True:
    username = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if username == admin and pwd == password:
        print("Login successful!")
        break
    else:
        print("Incorrect username or password. Please try again.")

while True:
    print("\nChoose a project to run:")
    print("1 for Number Guessing Game")
    print("2 for Simple Calculator")
    print("3 for Even-Odd Number Checker")
    print("4 for Voting Eligibility System")
    print("5 to Exit")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        # Project : number guessing game
        import random
        n = random.randint(1, 10)

        print("Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 10.")
        print("Try to guess it!")

        while True:
            number = int(input("Enter a number between 1 and 10: "))
            if number < n:
                print("Your guess is too low. Try again!")
            elif number > n:
                print("Your guess is too high. Try again!")
            else:
                print("Congratulations! You guessed the number correctly!")
                break

    elif choice == 2:
        # Project : Simple Calculator
        print("Welcome to the Simple Calculator!")
        print("Choose an operation:")
        print("1 for Addition")
        print("2 for Subtraction")
        print("3 for Multiplication")
        print("4 for Division")
        
        operation = input("Enter your choice (1-4): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation selected.")

    elif choice == 3:
        # Project : Even-Odd Number Checker + counter in range 
        n1 = int(input("Enter starting number: "))
        n2 = int(input("Enter ending number: "))
        c1 = 0
        c2 = 0
        for i in range(n1, n2 + 1):
            if i % 2 == 0:
                print(i, "is an even number")
                c1 += 1
            else:
                print(i, "is an odd number")
                c2 += 1
                
        print("Total even numbers:", c1)
        print("Total odd numbers:", c2)

    elif choice == 4:
        # Project : Voting Eligibility System 
        age = int(input("Enter your age: "))
        nationality = input("Enter your nationality: ")
        voter_id = input("Do you have a voter ID? (True/False): ")

        # Convert voter_id input to boolean
        voter_id_bool = voter_id.lower() == "true"

        if age >= 18 and (nationality.lower() == "indian") and voter_id_bool:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")

    elif choice == 5:
        print("Thank you for using the Basics Projects Interface. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid project number (1-5).")