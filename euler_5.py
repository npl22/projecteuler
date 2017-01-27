# Project Euler 5 Solution
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#very simple-minded solution
def solution_i():
  answer = 0
  i = 1
  while answer == 0:
    if i % 20 == 0:
      if i % 19 == 0:
        if i % 18 == 0:
          if i % 17 == 0:
            if i % 16 == 0:
              if i % 15 == 0:
                if i % 14 == 0:
                  if i % 13 == 0:
                    if i % 12 == 0:
                      if i % 11 == 0:
                        answer = i
    i += 1
  return answer


