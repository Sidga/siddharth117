# Assignment 3 ,8th question
set1 = {1,2,3,4,5}
set2 = {1,2,4,6,8}
set3 = {1,5,9,13,17}
#a
newset = set1.union(set2) - set1.intersection(set2)
print(newset)
#b
newset = set.union(set2).union(set3) - set1.intersection(set2) - set1.intersection(set3) - set2.intersection(set3)
print(newset)
#C
newset = set.intersection(set2).union(set1.intersection(set3)).union(set2.intersection(set3)) - set1.intersection(set2).intersection(set3)
print(newset)
#d
newset = set(range(1,26)) - set1
print(newset)
#e
newset = set(range(1,26)) - set1 - set2 -set3
print(newset)
#f
newset = set(range(1,26)) - set1.intersection(set2).intersection(set3)
print(newset)
