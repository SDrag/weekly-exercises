# Dragutin Sreckovic, 2018-03-04

# Iris data set formated printing:

# On the screen should be printed the petal length, petal width, 
# sepal length and sepal width, and these values should have the decimal 
# places aligned, with a space between the columns.

with open("data/iris.csv") as srcFile:
    for line in srcFile:
        cells = line.split(',')
# Since 'cells' is a list of strings, I'm converting them to floats 
# so I can use floating format just as an exercise (it would be the same result 
# if I just print them as they are because they are all the same length):
        print('{:1.1f} {:1.1f} {:1.1f} {:1.1f}'.format(float(cells[2]),float(cells[3]),float(cells[0]),float(cells[1])))
    
