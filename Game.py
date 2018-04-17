from Kakuro import Kakuro

x,y = input("Enter the Dimensions of the Kakuro Puzzle --> \t").split(",")
x = int(x)
y = int(y)

k = Kakuro(x, y)
k.build()