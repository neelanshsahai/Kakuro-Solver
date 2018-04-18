from Kakuro import Kakuro
from Solver import Solver

x,y = input("Enter the Dimensions of the Kakuro Puzzle --> \t").split(",")
x = int(x)
y = int(y)

k = Kakuro(x, y)
k.build()
solve = Solver(k)
k = solve.solve()
