#We make decisions based on conditions

temperature = 5

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: #(20, 30)
    print("It's a nice day")
elif temperature > 10: #(10, 20)
    print("It's a bit cold")
else: #This is executed if none of the above is true
    print("It's cold")
print('Done')