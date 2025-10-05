a, b = map(int,input().split())

total = 0
c = 2

if a % 2 != 0:
  a = a + 1

for i in range(a, b+1, c):
  total = total + i
print(total)
