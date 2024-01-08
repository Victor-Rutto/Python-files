# Membership operators

# Used to check presence of a element in a variable or list

a = 'Victor'
print ('r' in a)
b = [ 1, 2 ,4, 10, 'Victor'] 

#This gives error because we only find defined elements in the list
print('r' in b)
print('r' not in b) #True

#We have to find  defined characters: 1, 2 ,4, 10, 'Victor'
print(1 in b)
print(1 not in b) #False





