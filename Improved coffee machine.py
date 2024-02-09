# Exercise
menu = {"latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 10,
    }, 
    "cost": 100
    },
    "espresso":{
        "ingredients":{
            "water": 200,
            "milk": 100,
            "coffee": 10,
        }, 
        "cost": 200

    },
    "capuccino":{
        "ingredients":{
            "water": 150,
            "milk": 250,
            "coffee": 10,
        }, 
        "cost": 200

    }

}

resources = {
    "water": 1000,
    "coffee": 50,
    "milk": 700
}
revenue = 0
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]> resources[item]:
            print(f"sorry there is no {item} in stock")
            return False
    return True
def process_coins():
    print("Please insert coins ")
    total = 0
    ten = (int(input("How many 10 shillings coints? ")))
    twenty = (int(input("How many 20 shillings coints? ")))
    total = ten*10 + twenty*20
    print(total)
    return total

def is_payment_successful(total, coffee_cost):
    if total < coffee_cost:
        print(f"Sorry, {total} is not enought to pay for {choice}")
        shortage_money = coffee_cost - total
        additional_money=(input(f"Would you like to add {shortage_money} shillings to get your {choice} yes (y), no(n) ")).lower()
        if additional_money == "y":
            is_less_money =True
            while is_less_money:
                total += process_coins()
                if total> coffee_cost:
                    change= total-coffee_cost
                    print(f"Here is your {change} shillings change")
                    is_less_money= False
                    continue
                                  
                
        elif additional_money=="n":
            print(f"Your {total} is not enought to buy you {choice}")
            return False
        else:
            input("Please enter a valid response y/n ")
        return False
    else:
        change= total-coffee_cost
        global revenue
        revenue += coffee_cost
        print(f"Here is your {change} shillings change")
        return True
        
def make_coffee(coffee_choice, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_choice} ☕︎...... please enjoy")


is_on = True
while is_on:
    choice = input("What would you like to have? (Latte/espresso/cappuccino). ").lower()
    if choice == "off":
        is_on= False
    
    elif choice == "report":
        print(f"water is {resources['water']} ml")
        print(f"coffee is {resources['coffee']} grms")
        print(f"milk is {resources['milk']} ml")
        print(f"revenue is {revenue} shillings")
    else:
        coffee_type = menu[choice]
        # print(coffee_type)
        if check_resources(coffee_type['ingredients']):            
            payment= process_coins()
            if is_payment_successful (payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])




