import random
choicee = ["Rock", "Paper", "Scissors"]
user = input("Select your choice- Rock, Paper, or Scissors: ")
computer = random.choice(choicee)
print("You have chosen: ", user)
print("Computer has chosen: ", computer)
if user == computer:
    print("Both have the same choice so it's a tie!")
elif user == "Rock" and computer == "Scissors":
    print("You won this round!")
elif user == "Paper" and computer == "Rock":
    print("You won this round!")
elif user == "Scissors" and computer == "Paper":
    print("You won this round!")
else:
    print("Computer won this round!")