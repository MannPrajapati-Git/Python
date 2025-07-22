# user input 

name  = input("enter your name : ")
print("Hello", name )


# input method always takes input as string

# so if you want to take integer input, you need to convert it

age = input("enter your age : ")
age = int(age)  # converting string to integer
print("Your age is", age)

# you can direct use int() in input function as well
salary = int(input("enter your salary : "))
print("Your salary is", salary)

