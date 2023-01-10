# Python program to convert seconds into minutes and seconds
s = int(input("Enter seconds"))
m = s//60
s = s%60
print(m,"minutes",s,"seconds")
