# Project Euler 9 Solution
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2. For example, 32 + 42 = 9 + 16 = 25 = 52. There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

def solution_i(abc_sum: int) -> int:
  a, b, c = 1, 0, 0
  while a + b + c < abc_sum:
    b += 1
    c_2 = a ** 2 + b ** 2
    c = c_2 ** 0.5
    if a + b + c == abc_sum:
      break
    if a + b + c > abc_sum:
      a += 1
      b = a
  return int(a * b * c)
  
print(solution_i(1000))
