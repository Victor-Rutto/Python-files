# PAY BILL EXERCISE
name1= input("enter your names separated by a coma ")


friends = name1.split(",")
print([friends])

import random
length = len(friends)
random_choice=random.randint(0, length-1)

# computer_choice = random.choice(friends)
# print(computer_choice)
# print (random_choice)

# print(f"{random_choice} pays the bill")

print(f"{random.choice(friends)} pays the bill")



 
