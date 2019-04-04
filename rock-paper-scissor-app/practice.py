age = input("Enter your age: ")
if age:
	age = int(age)
	if age > 21:
		print("You are good to go!")
	elif age > 18:
		print ("You need to wear a wristband.")
	else:
		print("Nop! nono Nop!")
else:
	print("Please enter your age")		