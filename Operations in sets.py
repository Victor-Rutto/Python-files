set3={"Ram", "Sham", "Jan"}
set4 = {"Kim", "Jan", "Uhn"}
set5 ={1, 2, 3, 4}
# Unions 
# print(set3.union(set4))
# print(set3 | set4 | set5)
# print(set3.union(set4, set5))

# Unions in a set with a tuple 
# print(set3.union(('Tai', 'Kip')))

# Updating a set/Union update
set3.update(set4)
# print(set3)
# set3.update(['Kimuu', 'Taii', 'Radoo'])
# print(set3)
set6 = {'Kimuu', 'Taii', 'Radoo'}
set3 |= set6
print(set3)


# # Operations in sets

# set intersections
set1 ={1, 2, 3, 4, 5}
set2 = {4,5,6,7,8, 9}
print(set1.intersection(set2))
print(set1.intersection(['Kim', "Tai"]))
print(set1 & set2 & set3)

# Updating using intersection 
set1.intersection_update(set2) #This updates set1 with what is common in both sets.
print(set1)

# set difference
# print(set1-set2)