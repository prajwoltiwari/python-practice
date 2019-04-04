import random
computer_score = 0
player_score = 0
winning_score = 3

while computer_score < winning_score and player_score < winning_score:

	print(f"The computer score is {computer_score} and player score is {player_score}")
	print("\nROCK***PAPER***SCISSORS\n")

	player = input("Enter your move: ").lower()
	if player == "quit" or player == "q":
		break

	random_num = random.randint(0, 2)
	if random_num == 0:
		computer = "rock"
	elif random_num == 1:
		computer = "paper"
	else:
		computer = "scissors"

	print(f"Computer played {computer}")

	if player == computer:
		print("It's a tie")
	elif player == "rock":
		if computer == "paper":
			print("Computer wins!")
			computer_score += 1
		else:
			print("player wins!")
			player_score += 1
	elif player == "paper":
		if computer == "rock":
			print("Player wins!")
			player_score += 1
		else:
			print("Computer wins!")
			computer_score += 1
	elif player == "scissors":
		if computer == "rock":
			print("Computer wins!")
			computer_score += 1
		else:
			print("Player wins!")
			player_score += 1
	else:
		print("Enter a valid move!")

if player_score == computer_score:
	print("It's a tie.")
elif player_score > computer_score:
	print("Congrats. You won!!!")
else:
	print("\nOH NO!!! Computer won the game.")												
				
	

