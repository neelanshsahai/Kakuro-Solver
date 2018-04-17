class Block:

	_blocked = False;
	_number = False;
	_blank = False;

	_vertical = 0
	_horizontal = 0

	_actual_value = 0
	_possible_values = []



if __name__ == '__main__':

	x,y = input("Enter the Dimensions of the Kakuro Puzzle -->").split(",")
	x = int(x)
	y = int(y)

	kakuro = [[Block() for a in range(x)] for b in range(y)]

	for i in range(x):

		s = input().split(" ")

		for j in range(y):

			if(s[j] == '.'):
				kakuro[i][j]._blocked = True
				kakuro[i][j]._blank = False
				kakuro[i][j]._number = False
			elif(s[j] == '0'):
				kakuro[i][j]._blocked = False
				kakuro[i][j]._blank = True
				kakuro[i][j]._number = False
			else:
				kakuro[i][j]._blocked = False
				kakuro[i][j]._blank = False
				kakuro[i][j]._number = True

			if(kakuro[i][j]._blank):
				kakuro[i][j]._possible_values = [1,2,3,4,5,6,7,8,9]
			elif(kakuro[i][j]._number):
				v,h = s[j].split(",")
				kakuro[i][j]._vertical = int(v)
				kakuro[i][j]._horizontal = int(h)

	initialize()
