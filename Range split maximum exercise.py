# Range split maximum exercise
# Average-split range
# This program calculates the maximum height from a list of heights
# Takes input from users
# splits the inputs to form a list 
# use range to find the total number (n)

heights = input("Enter your heights separated by a coma ")

#168, 172, 153, 162, 166, 155
height_list = heights.split(',')

for i in range(0, len(height_list)): #0, 1, 2,3,4,5
    height_list[i]=int(height_list[i])
# print(len(height_list))
# print(height_list)
maximum_height = height_list[0]
for number in height_list:
    if number > maximum_height:
        maximum_height= number
print(f'maximum height is {maximum_height}')


