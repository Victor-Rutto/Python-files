import random as rm

print("Welcome to the random number generator Application")
print("The computer is going to guess a number within a range, try and guess the number for a prize. Good luck")

while True:
    computerguess = rm.randrange(1, 20)

    print()

    # Get user's guess as an integer
    userguess = input("Enter your guess number: ")

    if userguess == computerguess:
        print("You guessed the number correctly\n")
        print("You have won a big teddy bear")
    else:
        print("You guessed the wrong number. Try again.")