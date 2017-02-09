"""Project Euler 4 Solution.

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

def palindromic_number():
    """Find the largest palindormic number from 999 x 999."""
    result = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if (str(i * j) == str(i * j)[::-1]) and (i * j > result):
                result = i * j
    return result

# Notes for learning:
#[::-1] reverses a string using slicing,
#[:] makes a copy of the string :-1 -> :step number
#Thus, [::-1] is a copy of the string but in steps of -1
