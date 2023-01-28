list = []
count = 0
n = int()
while count <= 10:
    num = int(input("Enter the number"))
    count = count + 1
    print(list.insert(n,num))
print(list)
def numchar():
    for i in range(0,len(list)-1):
        if list[i] > 0:
            print(" This is a positive number")
        if list[i] < 0:
            print("This is a negative number")
        if list[i]%2 == 0:
            print("This is an even number")
        if list[i]%2 != 0:
            print("This is an odd number")

numchar()
