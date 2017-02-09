"""Project Euler 3.

What is the largest prime factor of the number 600851475143?

"""


def largest_prime_factor(number: int) -> int:
    """Find the largest prime factor of a number."""
    for i in range(2, int(number/2)+1):
        if number/i == round(number/i) and is_prime(int(number/i)):
            return int(number/i)

def is_prime(number: int) -> int:
    """Determine if a number is a prime number."""
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
