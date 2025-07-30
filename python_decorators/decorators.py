# decorators in python 
# A decorator is a function that takes another function as an argument, adds some functionality to it, and returns it.
# You apply a decorator using the @decorator_name



# most basic example

def function(func):
    def wrapper():
        return func()
    return wrapper

@function
def hello():
    return "hello"
result=hello()
print(result)

print("---------------------------------------------------------------------------------")

# example : timing function execution
# write a decorator that measures the time a function takes to execute.
import time 

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} : starting : {start} and ending : {end} so total time of run = {end-start} time")
        return result
    return wrapper

# this @  is decorator
@timer
def example_function(n):
    time.sleep(n)
example_function(2)


print("---------------------------------------------------------------------------------")

# example : debugging function calls 
# create a decorator to print the function name and the values of its arguments everytime the function is called 



def debug(func):
    def wrapper(*args,**kwargs):
        args_values=', '.join(str(arg) for arg in args)
        kwargs_values=', '.join(f"{k}:{v}" for k, v in kwargs.items())
        print(f"calling {func.__name__} function with args : {args_values}, and kwargs : {kwargs_values}")
        return func(*args,**kwargs)


    return wrapper



@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
greet("Mann", greeting="Welcome")


print("---------------------------------------------------------------------------------")


# example : cache return value
# implement a decorator that caches the return values of a function , so that when its called with the same arguments, the cached value is returned instead of re-executing the function.


import time


def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(7, 3))
print(long_running_function(17, 3))


# decorators with arguments 

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")
say_hi()