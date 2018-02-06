###################
### Exercise 1: ###
###################
def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 18
ans = fib(x)
print("Fibonacci number", x, "is", ans)

### My name is Dragutin, so the first and last letter of my name (D + N = 4 + 14) give the number 18. The 18th Fibonacci number is 2584.


###################
### Exercise 2: ###
###################

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Sreckovic"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

### My surname is Sreckovic
### The first letter S is number 83
### The last letter c is number 99
### Fibonacci number 182 is 48558529144435440119720805669229197641
### ord() function in Python: Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.