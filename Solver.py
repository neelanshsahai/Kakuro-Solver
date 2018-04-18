from Kakuro import Kakuro
from Block import Block


class Solver:

    def __init__(self, k):
        self.k = k

    def solve(self):
        for i in range(self.k.x):
            print()
            for j in range(self.k.y):
                print(self.k.kakuro[i][j]._actual_value, end=" ")

'''
. 5,6 0 0 0
. 0 . . .
. 0 . . .
. . . . .
. . . . .
'''