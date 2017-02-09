"""Project Euler 1 Solution.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def solution_i(number: int) -> int:
    """Find sum of multiples of 3 or 5 with a for loop and if statement."""
    result = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

def solution_ii(number: int) -> int:
    """Find sum of multiples of 3 or 5 using list comprehension."""
    return sum(x for x in range(1, number) if x % 3 == 0 or x % 5 == 0)
