# Average-split range
# This program calculates the average height from a list of heights
# Takes input from users
# splits the inputs to form a list 
# use range to find the total number (n)

heights = input("Enter your heights separated by a coma ")

height_list = heights.split(',')
# print(list_heights)
# for i in list_heights: this gives error
    # list_heights[i] = int(list_heights[i]) This is a string
count =0 #Using count to find the length
for height in height_list: #You can take any name in the place of height
    count = count+1
print(count)
for i in range(count):
    height_list[i] = int(height_list[i])
print(height_list)
total = 0
for person in height_list:
    total +=person
print(total)
avg = (total/count)
print(avg)




