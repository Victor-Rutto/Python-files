#NESTED IF AND ELIF ELSE STATEMENTS
height = int(input("Enter height in feet "))
if height>= 3:
    print("You can ride")
    age= int(input("enter age in years "))
    if age <= 12:
        print("Pay 100")
        print('Enjoy your ride')
    elif age <=15:
        print("pay 150")
        print('Enjoy your ride')
    elif age <= 18:
        print ("pay 200")
        print('Enjoy your ride')
    else:
        print("you are not a child")
        print("There are more things you can do as an adult")
else:
    print ("You are too young to ride")
print('Byee')
