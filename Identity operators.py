#Identity operators
#We have tow main types
# 1. Is 
# 2. Is not

# They basically compare memory locations of different variables.

#Is operators
# a = 5
# b = 5 
# print(a is b)
# print(id(a))
# print(id(b))

#Is not Operators
# print( a is not b)
 
#If we have two variables
a= 5
print(id(a))
a = 6

#The memory locations are different because integers are immutable. 
print(id(a))
print( a is a)



