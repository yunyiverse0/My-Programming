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
