# N = 3

# 1 3 5
# 7 9 1
# 3 5 7

N = int(input())
a = 1

for i in range(N):
    for j in range(N):
        print(a, end = ' ')
        a+=2
        if a > 9:
          a = 1
    print()
