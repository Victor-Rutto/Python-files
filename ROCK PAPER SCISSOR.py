# ROCK PAPER SCISSOR
rock = '✊'
paper = "✋"
scissor = '✌️'

game_choice = [rock, paper, scissor]

import random
player_choice = input("Enter your choice; Rock/Paper/Scissor")

if player_choice == 'Rock' or player_choice== 'rock' or player_choice=="ROCK":
    player_choice= 1
elif player_choice== 'paper' or player_choice== "Paper" or player_choice== "PAPER":
   player_choice=2
elif player_choice=='scissor' or player_choice== "Scissor" or player_choice== "SCISSOR":
    player_choice= 3
else:
    print("Invalid choice")
    exit()

computer_choice = random.randint(1,3)
print(game_choice[player_choice-1])
print(game_choice [computer_choice-1])

if player_choice == computer_choice:
    print("Draw")
elif player_choice== 2 and computer_choice==1:
    print("You win")
elif player_choice== 3 and computer_choice==1:
    print("You lose")   
elif player_choice > computer_choice:
    print('You win')
elif player_choice < computer_choice:
    print("You lose")
else:
    print("Invalid choice")
print("GAME OVER")

# import random

# player_choice = input("Enter your choice; Rock/Paper/Scissor: ").lower()

# if player_choice == 'rock':
#     player_choice = 1
# elif player_choice == 'paper':
#     player_choice = 2
# elif player_choice == 'scissor':
#     player_choice = 3
# else:
#     print("Invalid choice")
#     exit()

# computer_choice = random.randint(1, 3)
# print(f"Your choice: {player_choice}")
# print(f"Computer's choice: {computer_choice}")

# if player_choice == computer_choice:
#     print("Draw")
# elif (player_choice == 1 and computer_choice == 3) or \
#      (player_choice == 2 and computer_choice == 1) or \
#      (player_choice == 3 and computer_choice == 2):
#     print("You win")
# else:
#     print("You lose")

# print("GAME OVER")



