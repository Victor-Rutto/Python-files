# PASSWORD GENERATOR 
import random
# Using a loop to generate a list of letters from A to Z with both cases
# letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)]

# print("List of letters from A to Z with both cases:", letters)

letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
'Y', 'Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
'z']
numbers = [0, 1,2,3,4,5,6,7,8,9]
symbols = ['!', '#', '$', '%', '(', ')', '*', '+']

print("Welcome to password generator")
letters_input = int(input("How many letters do you want your passwpord to have? "))
numbers_input = int(input("How many letters do you want your passwpord to have? "))
symbols_input = int(input("How many letters do you want your passwpord to have? "))

password_list = []
for i in range(0,letters_input+1):
    char = random.choice(letters)
    password_list += char
for i in range(0,symbols_input+1):
    char = random.choice(symbols)
    password_list += char
for i in range(0,numbers_input+1):
    char = random.choice(numbers)
    password_list.append(char)
# password = random.shuffle(password)
# Note: shuffle only works on list.

print(password_list)
random.shuffle(password_list) 
print(password_list)
# Turning password to a string
password = ""
for char in password_list:
    password += str(char)
print(password)


# Letters_gen = ''.join(random.choice(letters(k =letters_input)))
# numbers_gen =''.join(random.choice(numbers(k=numbers_input)))
# symbols_gen = ''.join(random.choice(symbols(k=symbols_input)))

# print(Letters_gen)
# print(numbers_gen)
# print(numbers_gen)

