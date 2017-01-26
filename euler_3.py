# Project Euler 3 Solution
# What is the largest prime factor of the number 600851475143?

#takes ~38 seconds to solve
def largest_prime_factor(n: int) -> int:
  for i in range(2, int(n/2)+1):
    if n/i == round(n/i) and is_prime(int(n/i)):
      return int(n/i)
      
def is_prime(x: int) -> int:
  for num in range(2, x):
    if x % num == 0:
      return False
  else:
    return True
    
