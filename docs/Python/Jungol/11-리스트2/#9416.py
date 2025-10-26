# 3행 2열의 두 리스트 A와 B의 값들을 입력받아 두 배열의 합을 새로운 리스트에 저장하고 각 원소들을 2차원 형태로 출력하는 프로그램을 작성하시오.

##### MY CODE

A = []; B = []

for i in range(3):
    A.append(list(map(int,input().split())))
for i in range(3):
    B.append(list(map(int,input().split())))


for i in range(3):
    for j in range(2):
        print(A[i][j] + B[i][j], end = ' ')
    print()



##### GPT CODE

a = []
for i in range(3):
    a.append(list(map(int,input().split())))
b = []
for i in range(3):
    b.append(list(map(int,input().split())))

c = []
for i in range(3):
    sum = []
    for j in range(2):
        sum.append(a[i][j] + b[i][j])
    c.append(sum)

for i in c:
    print(i[0],i[1])
