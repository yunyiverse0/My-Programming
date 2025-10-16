#####################################9240
a, b = map(int,input().split())

a = print(a - b) if a >= b else print(b - a)

#####################################9241
N = int(input())

a = print('PLUS') if N > 0 else print()
a = print('MINUS') if N < 0 else print()
a = print('ZERO') if N == 0 else print()

#####################################9242
y = int(input())

a = print('leap year') if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else print('common year')

#####################################9243
a = int(input())

if a == 1:
    print('KOREA')
elif a == 2:
    print("USA")
elif a == 3:
    print('CHINA')
else:
    print('NO')

#####################################9227
a = int(input())

if a == 2:
    print(28)
elif  a < 8 and a % 2 == 1:
    print(31)
elif a >= 8 and a % 2 == 0:
    print(31)
else:
    print(30)

#####################################9228


#####################################9229
