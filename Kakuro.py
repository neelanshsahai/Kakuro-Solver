from Block import Block


class Kakuro:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kakuro = []

    def build(self):
        self.kakuro = [[Block() for a in range(self.x)] for b in range(self.y)]
        print("Now enter the Complete Board")

        for i in range(self.x):
            s = input().split(" ")
            for j in range(self.y):
                if s[j] == '.':
                    self.kakuro[i][j]._blocked = True
                    self.kakuro[i][j]._blank = False
                    self.kakuro[i][j]._number = False
                elif s[j] == '0':
                    self.kakuro[i][j]._blocked = False
                    self.kakuro[i][j]._blank = True
                    self.kakuro[i][j]._number = False
                else:
                    self.kakuro[i][j]._blocked = False
                    self.kakuro[i][j]._blank = False
                    self.kakuro[i][j]._number = True

                if self.kakuro[i][j]._blank:
                    self.kakuro[i][j]._possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    self.kakuro[i][j]._actual_value = "\t0\t"
                elif self.kakuro[i][j]._number:
                    v, h = s[j].split(",")
                    self.kakuro[i][j]._vertical = int(v)
                    self.kakuro[i][j]._horizontal = int(h)
                    self.kakuro[i][j]._actual_value = "\t"+v+"\\"+h+"\t"
                elif self.kakuro[i][j]._blocked:
                    self.kakuro[i][j]._actual_value = '\tX\t'
