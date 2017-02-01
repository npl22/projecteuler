#Project Euler 4 Solution
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindromic_number():
  result = 0
  for x in range (999, 99, -1):
    for y in range (999, 99, -1):
      if (str(x * y) == str(x * y)[::-1]) and (x * y > result):
        result = x * y
  return result

#[::-1] reverses a string using slicing, [:] makes a copy of the string :-1 -> :step number 
#so [::-1] is a copy of the string but in steps of -1
