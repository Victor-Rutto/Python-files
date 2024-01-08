# Range_function
# a = range(2,15, 3) #This skips 2 elements in the range 2-15
#argument stepwise(x) range(1,15, x) cannot be zero
# print(a[0])

# for i in a:
    # print(i)

# A program to calculate the total from 1-100
# count = 0
# for i in range (1, 101):
#     count +=i
# print(count)

total = 0
for i in range (1, 101):
    if i%2==0:
        total +=i
print(total)

total =0
for i in range(2,101, 2):
    total +=i
print(total)