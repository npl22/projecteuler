# Project Euler 7 Solution
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

def nth_prime(n: int) -> int:
  primes = [2]
  i = 1
  while len(primes) < n:
    i += 2
    for j in range(3, i, 2):
      if i % j == 0:
        break
    else:
      primes.append(i)
  return primes[-1]
  
#2nd solution, but takes just as long as the first solution
def nth_prime_ii(n: int) -> int:
  count = 4 #2, 3, 5, 7
  i = 9
  while count < n:
    i += 2
    if i % 3 == 0:
      continue
    if i % 5 == 0:
      continue
    for j in range(7, i, 2):
      if i % j == 0:
        break
    else:
      count += 1
  return i
  
