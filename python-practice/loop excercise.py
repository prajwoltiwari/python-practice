for x in range(1, 21):
	if x == 4 or x == 13:
		status = "unlucky"
	elif x%2 == 0:
		status = "even"
	else:
		status = "odd"
	print(f"You are {status}")	