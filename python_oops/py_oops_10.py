# MRO (Method Resolution Order)

# When a class inherits from multiple classes, MRO defines the order in which Python looks for methods.
# Python uses C3 Linearization for MRO.

# ClassName.__mro__  
# or  
# ClassName.mro()


class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):  # Multiple Inheritance
    pass

obj = D()
obj.greet()   # Output: Hello from B

print(D.__mro__)  # Method resolution order



# basic understanding

# ClassName.__mro__
# Returns a tuple of classes in MRO order.

class A: pass
class B(A): pass
class C(B): pass

print(C.__mro__)
# ➤ (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


# ClassName.mro()
# Returns a list of classes in MRO order (function form).


class A: pass
class B(A): pass
class C(B): pass

print(C.mro())
# ➤ [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
