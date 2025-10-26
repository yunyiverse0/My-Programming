a = map(int,input().split())
A = []
for i in a:
    n = (i // 10)
    A.append(n*10)

for i in range(100,-1,-10):
    if A.count(i) >= 1:
        print(f"{i}: {A.count(i)} person")
