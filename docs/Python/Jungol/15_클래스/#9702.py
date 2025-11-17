class j:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def __str__(self):
        return f'Name:{self.__name}, Age:{self.__age}'

N = int(input())

jlist = []
for i in range(N):
    name, age = input().split()
    jlist.append(j(name,age))

J = j(name, age)
jlist.sort(key = lambda x:x.getAge(), reverse = True)

for i in jlist:
    print(i)
