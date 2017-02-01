# Project Euler 1 Solution
# Find the sum of all the multiples of 3 or 5 __below__ 1000.

def solution_i(n: int) -> int:
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

def solution_ii(n: int) -> int:
    return sum(x for x in range(1, n) if x % 3 == 0 or x % 5 == 0)

