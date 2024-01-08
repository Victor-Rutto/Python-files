# MATRIX EXERCISE SOLUTION
row_1 = ["🤑", "🤑", "🤑"]
row_2 = ["🤑", "🤑", "🤑"]
row_3 = ["🤑", "🤑", "🤑"]

matrix = [row_1, row_2, row_3]

print(f"{row_1}\n{row_2}\n{row_3}")
player_choice = input("Enter your 2 digit number for the row and column ")

row_number = int(player_choice[0])
column_number = int(player_choice[1])

row_selected = matrix[row_number-1]
row_selected[column_number-1]='x'


# if players_choice == matrix [row_selected]:
#     print("congratulations you won")
# else:
#     print("Try again another time")
print(f"{row_1}\n{row_2}\n{row_3}")



