# Python program that prints out the sine and cosine of the angles ranging from 0 to 345  in 15 increments

from math import *
for i in range(0,360,15):
    print(i,"---",round(sin(i),4),round(cos(i),4))