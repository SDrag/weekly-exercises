# Dragutin Sreckovic, 2018-02-20

# Project Euler - problem 5 modified:
# Finding the smallest number that can be divided by each
# of the numbers from 1 to 20 without any remainder

# After running it got the following output:
#The smallest number that can be divided by each of the numbers from 1 to 20 without any remainder is: 232792560

notYetFound = True
finalNubmer = 20

while notYetFound:
    finalNubmer = finalNubmer + 10 #10 because it has to be divideable by both 2 and 10
    divideableByAll = True
    for i in range(2, 21):
        if finalNubmer % i > 0:
            divideableByAll = False
            break
    if divideableByAll:
        notYetFound = False

print("The smallest number that can be divided by each of the numbers from 1 to 20 without any remainder is:",finalNubmer)
