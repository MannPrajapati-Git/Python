# Project : Even-Odd Number Checker + counter in range 

n1=int(input("enter starting number :"))
n2=int(input("enter ending number : "))
c1=0
c2=0
for i in range(n1,n2+1):
    if i%2==0:
        print(i, "is an even number")
        c1 += 1
    else:
        print(i, "is an odd number")
        c2 += 1
        

print("Total even numbers:", c1)
print("Total odd numbers:", c2)