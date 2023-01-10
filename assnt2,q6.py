# Python program that take 3 sides as input and check whether a triangle can form or not 

a = int(input("Enter 1st side"))
b = int(input("Enter 2nd side"))
c = int(input("Enter 3rd side"))
if a < (b+c):
    print("Yes , it can form triangle")
elif a>(b+c)
    print("No ,it cant form triangle")
elif b < (a+c):
    print("Yes , it can form triangle")
elif c < (a+b):
    print("Yes, it can form triangle")

else:
    print("No, it can form triangle")
