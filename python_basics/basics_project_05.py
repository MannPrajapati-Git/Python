# project : Login Authentication System

correct_username = "mann"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Login failed! Incorrect username or password. Attempts left: {attempts}")
        if attempts == 0:
            print("Account blocked!")