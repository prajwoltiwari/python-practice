print("Rock...")
print("Paper...")
print("Scissors...")

Player1 = input("Player1 make your move: ")
print("***YOU CAN'T SEE THE NEXT PLAYER'S MOVE***\n\n" *27)
Player2 = input("Player2 make your move: ")

if Player1 == Player2:
	print("It's a tie!")
elif Player1 == "Rock":
	if Player2 == "Paper":
		print("Player2 wins!")
	elif Player2 == "Scissors":
		print("Player1 wins!")
elif Player1 == "Paper":
	if Player2 == "Rock":
		print ("Player1 wins!")
	elif Player2 == "Scissors":
		print("Player2 wins!")
elif Player1 == "Scissors":
	if Player2 == "Rock":
		print("Player2 wins!")
	elif Player2 == "Paper":
		print("Player1 wins!")
else:
	print("Something went wrong")									