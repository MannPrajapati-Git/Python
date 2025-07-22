# operators

# arithmetic operators
# + - * / % // **

no1= 10
no2=2
print("Addition:",(no1 + no2))  # addition
print("Subtraction:",(no1 - no2))  # subtraction
print("Multiplication:",(no1 * no2))  # multiplication
print("Division:",(no1 / no2))  # division
print("Modulus:",(no1 % no2))  # modulus
print("Floor Division:",(no1 // no2))  # floor division
print("Exponentiation:",(no1 ** no2))  # exponentiation

print("-------------------------------------------------------------")

# Assignment operators
# = += -= *= /= %= //= **=

no3 = 5
print("Value of no3:", no3)
no3 += 2  # no3 = no3 + 2
print("value of no3 += 2 is : ", no3)
no3 -= 1  # no3 = no3 - 1
print("value of no3 -= 1 is : ", no3)
no3 *= 3  # no3 = no3 * 3
print("value of no3 *= 3 is : ", no3)
no3 /= 2  # no3 = no3 / 2
print("value of no3 /= 2 is : ", no3)
no3 %= 2  # no3 = no3 % 2       
print("value of no3 %= 2 is : ", no3)
no3 //= 2  # no3 = no3 // 2
print("value of no3 //= 2 is : ", no3)
no3 **= 2  # no3 = no3 ** 2
print("value of no3 **= 2 is : ", no3)

print("-------------------------------------------------------------")

# Comparison/Relational operators
# == != > < >= <=

no4 = 10
no5 = 20
print("Is no4 equal to no5? : ", no4 == no5)  # equal
print("Is no4 not equal to no5? :", no4 != no5)  # not equal  
print("Is no4 greater than no5? :", no4 > no5)  # greater than
print("Is no4 less than no5? :", no4 < no5)  # less than
print("Is no4 greater than or equal to no5? :", no4 >= no5) # greater than or equal
print("Is no4 less than or equal to no5? :", no4 <= no5)  # less than or equal

print("-------------------------------------------------------------")

# Logical operators
# and or not

no6 = 10
no7 = 20
print(no6<no7 and no7<no6) # both conditions need to be true to get True output
print(no6<no7 or no7<no6) # one condition needs to be true to get True output
print(not (no6 == no7))  # True if no6 is not equal to no7

print("-------------------------------------------------------------")

# Bitwise operators
# & | ^ ~ << >> 

no8 = 10  # 1010 in binary
no9 = 20  # 10100 in binary

print("Bitwise AND (&):", no8 & no9)      # 0
print("Bitwise OR (|):", no8 | no9)       # 30
print("Bitwise XOR (^):", no8 ^ no9)      # 30
print("Bitwise NOT (~):", ~no8)           # -11
print("Bitwise left shift (<<):", no8 << 2)  # 40
print("Bitwise right shift (>>):", no9 >> 2) # 5

print("-------------------------------------------------------------")

# Membership operators
# in  not in

print("coffee" in "coffee aur code")  # True
print("tea" not in "coffee aur code")  # True

print("-------------------------------------------------------------")

# Identity operators
# is  is not

no10 = [1, 2, 3]
print(2 is no10[1])  # True
print(3 is not no10[2])  # False