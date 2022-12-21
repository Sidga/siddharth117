# python program to count the occurence  of a character

count = 0
my_string = input("Enter a string")
my_char = input("Enter the character")
for i in my_string:
    if i == my_char:
        count = count + 1
print(count)
