# break and continue statements in python

# break statement: exits the loop immediately
for i in range(10): 
    if i == 5:
        break
    print("Current value of i:", i)
    
print("--------------------------------------------------------------")
# continue statement: skips the current iteration and continues with the next iteration

for j in range(10):
    if j == 5:
        continue
    print("Current value of j:", j)

print("--------------------------------------------------------------")

# pass statement: does nothing, acts as a placeholder
for k in range(10):
    if k == 5:
        pass  # does nothing, just a placeholder
    print("Current value of k:", k)