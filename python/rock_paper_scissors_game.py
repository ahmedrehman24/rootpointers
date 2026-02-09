import random

choices = ["rock", "paper", "scissors"]

while True:
    player = input("rock/paper/scissors (q to quit): ").lower()
    if player == "q":
        break

    computer = random.choice(choices)
    print("Computer:", computer)

    if player == computer:
        print("Tie")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
