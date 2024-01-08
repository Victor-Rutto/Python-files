#F STRINGS IN PYTHON
name = "victor"
age = 30
height = 1.56

#The methods are prone to errous
# 1. use of + 
print("my name is " +name, "I am"  +str(age), "years old")
# 2. Use of ,
print("My name is " ,name, "I am " ,age, "years old", "my height is " ,height, 'meters')

#Solution
print(f"my name is {name} and I am {age}, my height is {height}")

#We can evaluate variables like age
print(f"My father is {age*2} old")
