lower = int(input("Enter the lower limit"))
upper = int(input("Enter the upper limit"))
num = int(input("Enter the number"))
for i in range(lower,upper+1):
    if i%num == 0:
        print(i)
