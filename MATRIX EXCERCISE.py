# MATRIX EXCERCISE
player_name = input("Enter your name ")
player_choice = int(input("enter 2 digits of the 3*3 matrix "))



matrix = [[11, 12, 13],[21, 22, 23],[31, 32, 33]]
length = len(matrix)
print(length)
print(matrix [1][1])

if player_choice == matrix [1][1]:
    print(f'congratulations {player_name} you have won yourself Azubi ticket')
else:
    print("Try next time")
print(f'Byee {player_name}')

