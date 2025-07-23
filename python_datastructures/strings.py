# strings in python

# introduction to strings
# strings are immutable
# strings are sequences of characters
# strings can be sliced and indexed
# strings can be concatenated


name="Mann Prajapati"
print("introduction to strings")
print("The name is :",name)
first_character=name[0]
print("first character is :",first_character)
slice_name=name[0:5]
print("slicing the name :",slice_name)
negative_slice=name[-1]
print("you can also do negative slices :",negative_slice)
print("----------------------------------------------------")


# String concatenation example
first_name = "Mann"
last_name = "Prajapati"
full_name = first_name + " " + last_name
print("Concatenated name:", full_name)

print("---------------------------------------------------")


print("String slicing examples:")
number_list="0123456789"
print(number_list[:])
print(number_list[3:])
print(number_list[:6])
print(number_list[3:6])
print(number_list[0:7:2])
print(number_list[0:7:3])


print("---------------------------------------------------")

# String methods 
print("String methods examples:")
company="Coffee Aur Code"
print("lower case:", company.lower()) # converts to lowercase
print("upper case:", company.upper()) # converts to uppercase
print("striped text :", company.strip()) # removes leading and trailing whitespace
print("replaced text:", company.replace("Coffee Aur Code", "CodeWithMannSir")) # replaces a substring
print("split text:", company.split()) # splits the string into a list 
print("the length is :",len(company)) # gets the length of the string

print("----------------------------------------------------")
# string validation methods
name = "Mann123"
print(name.isalnum())  # True
print(name.isalpha())  # False
print(name.isdigit())  # False
print(name.islower())  # False
print(name.isupper())  # False
print(name.isnumeric())  # False
print(name.isspace())  # False

print("---------------------------------------------------")

# try below also 
# try_string="Mann, heli, roshni, divyang"
# print("split with comma:", try_string.split()) 
# output -> ['Mann,', 'heli,', 'roshni,', 'divyang']
# you can see above output, it has two comma and spliting with comma
# to over come this, you can use below code
# print("split with comma:", try_string.split(","))
# output -> ['Mann', ' heli', ' roshni', ' divyang']

print("find method:", company.find("Code")) # finds the index of a substring
# in find method if there is no substring found, it returns -1

print("count method:", company.count("o")) # counts occurrences of a substring
# in count method if there is no substring found, it returns 0

offices=2
statement="I am CEO of {} and I have {} offices"
print(statement.format(company, offices)) # formats the string with variables

# but these method is old and you can use f-string like below
print(f"I am CEO of {company} and I have {offices} offices") # f-string formatting


# list to string
company_names=["CodeWithMannSir", "Coffee Aur Code"]
string_formate=print(",".join(company_names)) # joins a list of strings into a single string
#you can add space or everything you want in between the list elements inside the double quotes-> " "  ","  "-"  etc etc




for i in company:
    print(i) # iterating through each character in the string



print("---------------------------------------------------")

# Escape characters in strings and concept of raw strings
# Escape characters are used to insert special characters in strings
# raw strings are used to ignore escape characters
# common escape characters are: \n (newline), \t (tab), \\ (backslash), \' (single quote), \" (double quote)
compliment1="1. Every Student said, \"MannSir is a Good Teacher\" "
print(compliment1) # using escape character to print quotes inside a string

compliment2="2. Every Student said,\n\"MannSir is a Good Teacher\" "
print(compliment2) # using escape character to print quotes inside a string with newline


#but if you want to print \n as it is, you can use row string
compliment3=r"3. Every Student said,\n\"MannSir is a Good Teacher\" "
print(compliment3) # using raw string to print \n as it is

# important for path handleing like -> c:\\Users/Mann/Desktop 

print("---------------------------------------------------")

# you can ask questions to string like below (just for knowledge)
sentence= "Mann Prajapati is a good teacher"
print("Mann"in sentence) # checks if "Mann" is in the sentence
print("mann"in sentence) # checks if "mann" is in the sentence (case sensitive)