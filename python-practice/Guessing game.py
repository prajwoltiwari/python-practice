import random
computer = random.randint(1, 10)
while True:
	guess = input("Enter your guess: ")
	guess = int(guess)
	print(guess)
	if guess < computer:
		print("That is too low.")
	elif guess > computer:
		print("That is too high")
	else:
		print("Yatta!!! You won!")
		again = input("Do you wanna play again? (y/n) ")
		if again == "y":
			computer = random.randint(1, 10)
			guess = None
		else:
			print("Thank you for playing. :)")
			break	
