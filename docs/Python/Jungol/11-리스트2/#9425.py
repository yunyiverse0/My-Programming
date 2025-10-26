a = [input().split() for _ in range(3)]

for i in a:
    for j in i:
        print(j.lower(), end=' ')
    print()
