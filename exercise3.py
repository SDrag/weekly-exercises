# Dragutin Sreckovic 2018-02-07
# Collatz conjecture

# Asking user for an integer:
userInput = input("Please enter an integer greater then 0: ")

# Checking if it's an integer greater then 0. If not use a default value:
defaultVal = 27
try:
	val = int(userInput)
	if val == 0:
		print("That's not what I've asked for! Will use", defaultVal, "instead.")
		val = defaultVal
except ValueError:
	print("That's not what I've asked for! Will use", defaultVal, "instead.")
	val = defaultVal

# Applying Collatz conjecture until it reaches 1
while val > 1:
	print(val, end=', ')
	if val % 2 == 0:
		val = int(val / 2)
	else:
		val = val * 3 + 1

#Printing the last member (1):		
print(val)
	
