import random
print("Welcome to the multiplication game")
for num in range(0,10):
    num1 = random.randint(2,12)
    num2 = random.randint(2,12)
    answer = num1*num2

    print("What is",num1,"x",num2,":")
    guess = int(input("Answer :"))
    if guess == answer:
        print("This is the correct answer")
    elif guess != answer:
        print("No,This is the incorrect answer ")
else:
    print("Please enter a valid answer")


