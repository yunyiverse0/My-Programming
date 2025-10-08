# 2부터 9까지의 정수 S와 E를 입력받아 S단부터 E단까지의 구구단을 차례대로 출력하는 프로그램을 작성하시오.
# (2 ≤ S,E ≤ 9, 구구단 사이의 공백은 3칸이다.)


S = int(input())
E = int(input())

if S < E:
    a = S; b = E; c = 1
else:
    a = S; b = E; c = -1

for i in range(1, 10, 1):
  for j in range(a, b + c, c):
    print(f"{j} * {i} = {i*j}", end = "   ")
  print( )
