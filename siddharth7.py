# Python program to show next date by asking date as input 

day = int(input("Enter the day"))
month = int(input("Enter the month"))
year = int(input("Enter the year"))
if month >12:
    print("please enter a valid month")
    day = int(input("Enter the day"))
    month = int(input("Enter the month"))
    year = int(input("Enter the year"))
elif year >2025 and year < 1800:
    print("please enter a valid year")
    day = int(input("Enter the day"))
    month = int(input("Enter the month"))
    year = int(input("Enter the year"))
elif day > 31:
    print("please enter a valid day ")
    day = int(input("Enter the day"))
    month = int(input("Enter the month"))
    year = int(input("Enter the year"))

day = day + 1
print("Next Date is",day,"/",month,"/",year)

