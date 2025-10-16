################################9217
a = int(input())
b = int(input())
c = int(input())
d = int(input())
tot = a + b + c + d

print(f'''tot: {tot}
avg: {tot/4:.0f}''')
################################9218
N, M = map(int,input().split())

print((N//M)*(N%M))

################################9219
a = int(input())
b = int(input())

a = a * 2
b = b - 3

print(f'''width = {a}
length = {b}
area = {a*b}''')

################################9220
A, B, C = map(int,input().split())

print((A*B*C)-(A+B+C))

################################9221
a, h = map(int,input().split())
A, H = map(int,input().split())

a = True if A > a and H > h else False

print(a)

################################9222
x = True; y = False

print('x and y ->',x and y)
print('x or y ->',x or y)
print('not x ->',not x)
print('not y ->',not y)
