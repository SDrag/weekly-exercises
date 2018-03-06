# Dragutin Sreckovic, 2018-03-06

# Function for factorial calculation of a given number:

def factorial(n):
	fact = 1
	for i in range(n, 1, -1):
		fact = fact * i
	return fact


print(factorial(5))		# prints 120
print(factorial(7))		# prints 5040
print(factorial(10))	# prints 3628800

# For the completeness, we should also test if 'n' is a positive integer