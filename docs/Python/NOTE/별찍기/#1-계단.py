#####계단
N = int(input())

for i in range(N):            # N = 5, i = 1,2,3,4
  print(' ' * i , end='')
  print('*' * N)


#####삼각형
# 왼쪽정렬 삼각형
n = int(input())

for i in range(1, n + 1):
  print('*' * i)          #공백X
  
# 오른쪽정렬 삼각형

n = int(input())

for i in range(1, n + 1):
  print(' ' * (n - i), end = '')
  print('*' * i)

# 역삼각형
n = int(input())

for i in range(N):
  print('*' * (N - i))
