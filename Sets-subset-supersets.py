# Sets-subset-supersets
# 1. Disjoin sets- sets that have nothing in common
set1 = {1,2,3,4,5, }
set2 = {4,10,7,8, -10}
# set1.isdisjoint(set2) #False

# subsets
# set 1 is a subset of set2 if all elements of set 1 are in set 2 
# set1.issubset(set1)
print(set1.issubset(['Miriam', "john"]))
# print(set1 <= set2)
# set1.update({20, 30, 40})
# print(set1)

# supersets
# Set1 is a superset if it has all elements of set 2
print(set1.issuperset(set2))
print(set1 >= set2)
# set set1 deletes all the set 










































