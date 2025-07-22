# variables and datatypes

# variable : a container for storing data values
# variable names must start with a letter or underscore, followed by letters, numbers, or underscores

name = "Mann" 
age = 21
height = 5.9
ai = True

print("Name :",name)
print("Age :",age)
print("Height :",height)
print("Anger issue ?  :",ai)
print("-------------------------------------------------------------")

# so from the above example -> name,age,height,ai are variables
# and "Mann", 21, 5.9, True are values assigned to those variables

# datatypes : the type of data a variable can hold
# common datatypes in python are: string, integer, float, boolean

# "mann" is a string
# 21 is an integer
# 5.9 is a float
# True is a boolean

# type checking 

# type() function returns the type of the variable

print("Type of name :", type(name))  # <class 'str'>
print("Type of age :", type(age))    # <class 'int'>        
print("Type of height :", type(height))  # <class 'float'>
print("Type of ai :", type(ai))  # <class 'bool'>

print("-------------------------------------------------------------")

# type conversion : converting one datatype to another
# int() function converts a value to an integer
# float() function converts a value to a float
# str() function converts a value to a string
# bool() function converts a value to a boolean

age_str = str(age)  # converting integer to string
height_int = int(height)  # converting float to integer

print("type of age_str :", type(age_str))  # <class 'str'>
print("type of height_int :", type(height_int))  # <class 'int'>