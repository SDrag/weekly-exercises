# Dragutin Sreckovic, 2018-02-20

# Project Euler - problem 5 modified:
# Finding the smallest number that can be divided by each
# of the numbers from 1 to 20 without any remainder

# After running it got the following output:
# The smallest number that can be divided by each of the numbers from 1 to 20 without any remainder is: 232792560

notYetFound = True   # Variable which gets False when we find our number -> exit while loop
finalNubmer = 20     # Variable that holds the number we are checking

# Loop until the number is found -> notYetFound becomes False:
while notYetFound:
    finalNubmer = finalNubmer + 20   # Increment by 20 because it has to be divideable by both 2 and 10
    divideableByAll = True           # Assume True and try to dissaprove it
    # Check if dividible by all the numbers in the range except 1:
    for i in range(2, 21):
        if finalNubmer % i > 0:
            divideableByAll = False  # Not dividible by this number, so set it to False
            break                    # Break the for loop since we found at least one number which does'n satisfy criteria
    # Check if the number is divideable by all:
    if divideableByAll:
        notYetFound = False          # If we found our number, set this to False so we can exit while loop

# Print the result:
print("The smallest number that can be divided by each of the numbers from 1 to 20 without any remainder is:",finalNubmer)
