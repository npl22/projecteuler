"""Project Euler 18 Solution.

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.
     3
    7 4
   2 4 6
  8 5 9 3
 That is, 3 + 7 + 4 + 9 = 23.

 Find the maximum total from top to bottom of the triangle (imported from file)
 15 rows

"""

def solution_i():
    """Calculate the solution for Project Euler #18.

    1) Import a file with the triangle
    2) Read the file and convert it into a nested array of integers
    3) Find the max of each pair starting at the bottom and sum to the top

    """
    tri = [list(map(int, i.split())) for i in open('e18_input.txt').readlines()]
    for row in range(len(tri)-1, 0, -1):
        for i in range(0, len(tri[row])-1):
            tri[row-1][i] += max(tri[row][i], tri[row][i+1])
    return tri[0]
