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
