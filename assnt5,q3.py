a = int(input("Enter the first side of triangle"))
b = int(input("Enter the second side of triangle"))
c = int(input("Enter the third side of triangle"))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The Area of the triangle is",area)