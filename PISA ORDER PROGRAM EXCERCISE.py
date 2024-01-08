#PISA ORDER PROGRAM


size = input("what size of pisa do you want? Small (S), medium (M) or large (L) ")
bill = 0
if size == 'S' or size== "s":
    bill += 100
    print(f"small size pisa is {bill}")
elif size == "M" or size== "m":
    bill = bill + 200
    print(f" medium size pisa is {bill}")
else:
    bill = bill + 300
    print(f"large size pisa bill is {bill}")
pepperoni = input("Add pepperoni for pisa? Y/N ")
if pepperoni == 'Y' or pepperoni=="y":
    if size == 'S' or size== "s":
        bill += 30
    else:
        bill += 50
        print(f"your bill is {bill}")
cheese= input("Want extra cheese for any size? Y/N ")
if cheese == "y" or cheese=="Y":
    bill += 20
    print (f"your bill is {bill}")
else:
    print(f"your total bill is {bill}. Please enjoy your pisa")







