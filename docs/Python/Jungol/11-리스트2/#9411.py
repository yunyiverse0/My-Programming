# 2행 3열의 2차원 리스트를 입력받아, 전체 리스트를 출력하고, 각 행 단위로 리스트를 출력하고, 각 원소를 2행 3열에 맞추어 출력하는 프로그램을 작성하시오.

##### MY CODE

a = list(map(int,input().split()))
b = list(map(int,input().split()))


print([a,b])
print(a)
print(b)
print(*a)
print(*b)

##### GPT CODE

a = []

for i in range(2):
    C = list(map(int,input().split()))

    a.append(C)

print(a)

for row in a:
    print(row)

for row in a:
    for x in row:
        print(x, end=' ')
    print()
