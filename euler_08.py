"""Project Euler 8.

The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832. Find the thirteen adjacent digits in the
1000-digit number that have the greatest product. What is the this product?

"""

def solution_i(digits: int) -> int:
    """Find the largest product of x adjacent digits in a large number."""
    huge_number = int(open('input_files/e08_input.txt').read())
    print(huge_number)

    answer = 0
    i = 0
    while i < (len(str(huge_number)) - digits):
        product = 1
        for j in range(i, i + digits):
            product *= int(str(huge_number)[j])
            if product > answer:
                answer = product
        i += 1
    return answer

print(solution_i(13))
