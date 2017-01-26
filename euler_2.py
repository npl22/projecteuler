# Project Euler 2 Solution
# Find the sum of all the even numbers of the fibonacci sequence up to four million.
# The starting terms are 1, 2 (e.g. 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...)

def solution_i(x: int) -> int:
  fibonacci = [1, 2]
  i = 2 #start index at 2 for recursive/fibonacci sequence
  j = 0
  last_number = 0
  result = 2 #start at 2 because first two numbers in sequence aren't included in loop
  while last_number < x:
    if j == fibonacci[i-1] + fibonacci[i-2]:
      fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
      last_number = fibonacci[i]
      if fibonacci[i] % 2 == 0:
        result += fibonacci[i]
      i += 1
    j += 1
    
  return result
#Iterates through numbers 1 to x (while last_number < x:)
#1st conditional statement is used to generate an array for fibonacci numbers
#2nd conditional statement is used to find the cumulative sum of the even numbers in the sequence

def solution_ii(upper_limit: int) -> int:
  a,b = 1, 2
  result = 2
  while b < upper_limit:
    a, b = b, a+b
    if b % 2 == 0:
      result += b
      
  return result
