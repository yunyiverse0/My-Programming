# 왼쪽정렬 삼각형
n = int(input())

for i in range(1, n + 1):
  print('*' * i)          #공백X
  
# 오른쪽정렬 삼각형

n = int(input())

for i in range(1, n + 1):
  print(' ' * (n - i), end = '')
  print('*' * i)
