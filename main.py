import random

player_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

print("=== Rock Paper Scissors ===")

while True:
    player = input("\nChoose Rock, Paper, or Scissors (or Q to quit): ").capitalize()

    if player == "Q":
        break

    if player not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("Draw!")

    elif (
        (player == "Rock" and computer == "Scissors")
        or (player == "Paper" and computer == "Rock")
        or (player == "Scissors" and computer == "Paper")
    ):
        print("You Win!")
        player_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("Score:", player_score, "-", computer_score)

print("\nFinal Score:")
print("Player:", player_score)
print("Computer:", computer_score)
print("Thanks for playing!")