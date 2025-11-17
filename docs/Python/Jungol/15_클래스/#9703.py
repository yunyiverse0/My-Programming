class j:
    def __init__(self, X, Y):
        self.__X = X
        self.__Y = Y
    
    def getx(self):
        return self.__X

    def gety(self):
        return self.__Y

    def __str__(self):
        return f'({self.__X}, {self.__Y})'

N = int(input())

jlist = []
for _ in range(N):
    x, y = input().split()
    x = float(x)
    y = float(y)
    jlist.append(j(x, y))

jlist.sort(key=lambda x: x.getx())

for i in jlist:
    print(i)
