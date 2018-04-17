from Block import Block


class Kakuro:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def build(self):
        kakuro = [[Block() for a in range(self.x)] for b in range(self.y)]
        print("Now enter the Complete Board")

        for i in range(self.x):
            s = input().split(" ")
            for j in range(self.y):
                if (s[j] == '.'):
                    kakuro[i][j]._blocked = True
                    kakuro[i][j]._blank = False
                    kakuro[i][j]._number = False
                elif (s[j] == '0'):
                    kakuro[i][j]._blocked = False
                    kakuro[i][j]._blank = True
                    kakuro[i][j]._number = False
                else:
                    kakuro[i][j]._blocked = False
                    kakuro[i][j]._blank = False
                    kakuro[i][j]._number = True

                if (kakuro[i][j]._blank):
                    kakuro[i][j]._possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                elif (kakuro[i][j]._number):
                    v, h = s[j].split(",")
                    kakuro[i][j]._vertical = int(v)
                    kakuro[i][j]._horizontal = int(h)
