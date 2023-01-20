def palindrome():
    str = input("Enter a string ")
    if str == str[::-1]:
        print("This is a palindrome")
    elif str != str[::-1]:
        print("This is not a palindrome")
    else:
        print("Please enter a valid string")
palindrome()