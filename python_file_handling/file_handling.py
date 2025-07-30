# file handling in python
# Python provides built-in functions to handle file operations like reading, writing, appending, deleting, and more.

# Open a File

# Modes
# 'r': Read : (default) Opens file for reading
# 'w': Write : Creates file if not exists, overwrites if exists
# 'a': Append : Appends to end of file
# 'x': Create : Creates file, error if exists
# 'b': Binary : For binary files (e.g., images)
# 't': Text	: Text mode (default)
# '+':  Read/Write : Updates file


# Read Entire File
f = open("python_file_handling/document.txt", "r") # opens the file  # "r" stands for read mode
result = f.read() # .read() reads the entire content of the file at once as a single string.
print(result)
f.close() # closes the file

#Read Line-by-Line
f = open("python_file_handling/document.txt", "r")
for line in f:
    print(line.strip())
f.close()

# Read First Line Only
f = open("python_file_handling/document.txt", "r")
print(f.readline())  # Only first line
f.close()

# Read All Lines into List
f = open("python_file_handling/document.txt", "r")
lines = f.readlines()
print(lines)
f.close()

print("--------------------------------------------------------------------------")

# Writing to a File
# Overwrites everything!
f = open("python_file_handling/document.txt", "w")
f.write("Hello, MannSir!\nWelcome to Python.")
f.close()

# Appending to a File
# It adds text at the end without deleting old content.
f = open("python_file_handling/document.txt", "a")
f.write("\nBasics To Advanced journey.")
f.close()


# Using with Statement
# Automatically handles .close()
with open("python_file_handling/document.txt", "r") as f:
    content = f.read()
    print(content)

# Read and Write Both
with open("python_file_handling/document.txt", "r+") as f:
    data = f.read()
    f.write("\nNew data added while reading.")


# Creating New File Safely
#  Throws error if file already exists.
f = open("python_file_handling/document2.txt", "x")
# f = open("document.txt", "x") # this will throw error
f.write("This repository is very helpful to learn python from basics to advanced")
f.close()

#  Get File Info (Metadata)
f = open("python_file_handling/document2.txt", "r")
print(f.name)
print(f.mode)
print(f.closed)
f.close()
print(f.closed)

# Delete a File
import os
os.remove("python_file_handling/document2.txt")

#  Check If File Exists Before Deleting
import os
if os.path.exists("python_file_handling/document2.txt"):
    os.remove("python_file_handling/document2.txt")
else:
    print("File not found.")


# Create / Remove Folder
import os
os.mkdir("myfolder")       # Create folder
os.rmdir("myfolder")       # Remove empty folder


# Truncate a File
#  this shortens the file to 10 bytes
f = open("python_file_handling/document.txt", "r+")
f.truncate(10)  # Keep only first 10 characters
f.close()


# read binary file
with open("python_file_handling/image.jpeg", "rb") as img:
    data = img.read()
print(data)
print(data[:10])  # show first 10 bytes
print(len(data), "bytes read")
