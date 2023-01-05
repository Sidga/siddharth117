#Python program to take marks as input and give grade as output

m = int(input("Enter your marks"))
if 0<=m<25:
    print("Your grade is F")
elif 25<=m<45:
    print("Your grade is E")
elif 45<=m<50:
    print("Your grade is D")
elif 50<=m<60:
    print("Your grade is C")
elif 60<=m<80:
    print("Your grade is B")
elif 80<=m<100:
    print("Your grade is A")
else:
    print("Please enter the valid marks")