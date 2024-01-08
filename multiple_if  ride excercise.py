bill = 0
height = int(input("Enter height in feet "))
if height>= 3:
    print("You can ride")
    age= int(input("enter age in years "))
    if age <= 12:
        bill = 100
        print("Ticket price is Pay 100")
        print('Enjoy your ride')
    elif age <=15:
        bill = 200
        print("Ticket price is Pay 200")
        print('Enjoy your ride')
    elif age <= 18:
        bill = 300
        print("Ticket price is Pay 300")
        print('Enjoy your ride')
    else:
        print("you are not a child")
        print("There are more things you can do as an adult")
    photo= input("Do you want to take photos? Y/N ")
    if photo == "Y" or photo == "y":
        bill = bill + 50
    print(f"Your total ticket is {bill}")
else:
    print ("You are too young to ride")
print('Thank you, enjoy the ride')
