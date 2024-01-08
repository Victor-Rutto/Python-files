# set methods - symetric difference
# symetric-difference_update
set1 ={1, 2, 3, 4, 5}
set2 = {4,5,6,7,8, 9}
set3 = {13, 14, 15}
# set difference 
# print(set1.difference(set2)) #Items in set1 but not in set 2
# print(set1.difference("Jim", "Jun"))
# print(set1- set2 - set3) #Items in set1 but not in either of the rest

# Difference_update method
# set2.difference_update(set1)
# print(set2)

# symetric difference_update
# Returns all elements not in both
# print(set1.symmetric_difference(set1))

# print(set1^set2)
set2.symmetric_difference_update(set1)
print(set2)




