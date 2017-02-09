"""Project Euler 2 Solution.

Find the sum of all the even numbers of the fibonacci sequence up to four million.
The starting terms are 1, 2 (e.g. 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...)

"""

#Iterates through numbers 1 to x (while last_number < x:)
#1st conditional statement is used to generate an array for fibonacci numbers
#2nd conditional statement is used to find the  sum of the even numbers
def solution_i(a_n: int) -> int:
    """Calculate the sum of all the even fibonacci numbers."""
    fibonacci = [1, 2]
    i = 2
    j = 0
    last_number = 0
    result = 2
    while last_number < a_n:
        if j == fibonacci[i-1] + fibonacci[i-2]:
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
            last_number = fibonacci[i]
            if fibonacci[i] % 2 == 0:
                result += fibonacci[i]
            i += 1
        j += 1

    return result


def solution_ii(upper_limit: int) -> int:
    """Calculate the sum of all the even fibonacci numbers."""
    a_1, a_2 = 1, 2
    result = 2
    while a_2 < upper_limit:
        a_1, a_2 = a_2, a_1 + a_2
        if a_2 % 2 == 0:
            result += a_2

    return result
