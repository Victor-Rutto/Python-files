# FOR ELSE 
# for var_name in sequence:
#     statement(s)
# else:
#     statement(s)
# NOTE : The else statement is only executed if for is successful.

# numbers = [1,2, 3,4, 5]
# for i in numbers:
#     print(i)
# else:
#     print("successfully completed")

# If there is a break in the for section, the program will terminate there
# numbers = [1,2, 3,0, 4, 5]
# for i in numbers:
#     print(i)
#     if i==0:    
#         break
# else:
#     print("successfully completed")


tuple1= (2,56, 34,3,5,-1)
for i in tuple1:
    # print(i)
    if i %6 ==0:
        print(i)
        break
    # else:
    #     print("There is no number divisible by 6 in this sequence")
else:
    print("There is no number divisible by 6 in this sequence")



 