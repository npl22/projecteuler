"""Project Euler 10 Solution.

Find the sum of all the primes below two million.

Hint 1: Any number n can have only one primefactor greater than sqrt(n).
You have a number 'N²'. If it has a factor J < N, then the other factor has to
be greater than N. Hence, when you check that J is a factor of N, effectively
you check the other factor also.

Hint 2: Use the Sieve of Eratothenes method.
Start from the first prime number 2, iteratively mark the multiples of each
prime number as composite (not prime). For example, note 2 and 3 as prime and
remove all of their multiples up to n. The next number to be checked would be
5 since 4 is a multiple of 2 and was removed. This is much faster than using
modular division to check.

"""
import math

#too slow
def sum_of_primes_i(number: int) -> int:
    """Find the sum of all primes less than than a certain number."""
    prime = []
    not_prime = []
    for i in range(2, number+1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i*i, number+1, i):
                not_prime.append(j)

def sum_of_primes_ii(number: int) -> int:
    """Find the sum of all primes less than than a certain number."""
    primes = [True] * (number + 1)
    primes[0] = primes[1] = False
    for i in range(2, math.ceil(number**0.5) + 1):
        if primes[i]:
            for j in range(i*i, number+1, i):
                primes[j] = False
    return sum(i for i in range(2, number+1) if primes[i])

print(sum_of_primes_ii(2000000))

#Notes: i*i, example, for i = 5, you already did 2*5 and 3*5 in the previous
#iterations (and 4*5 is a multiple of 2) so you can start at 5*5 or i*i
