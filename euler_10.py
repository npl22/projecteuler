"""Project Euler 10 Solution.

Find the sum of all the primes below two million.

"""

def solution_i(n: int) -> int:
    """Find the sum of all primes less than than a certain number."""
    for i in range(2, n+1):
