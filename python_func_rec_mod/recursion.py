# recursive function

# What is Recursion?
# A recursive function is a function that calls itself to solve a smaller subproblem.
# But: Every recursion must have 2 parts:
# Base Case → Where the function stops calling itself (stopping condition)
# Recursive Case → Where function calls itself with modified input


# find factorial using recursion in functions

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

# find fibonacci series using recursion in function

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

for i in range(6):
    print(fib(i), end=' ')
