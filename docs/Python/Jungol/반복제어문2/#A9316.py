# 두 개의 정수 S와 E를 입력받아서 작은 수부터 큰 수까지 차례대로 출력하는 프로그램을 작성하시오.

S, E = map(int,input().split())
a = 0 
b = 0

if S < E:
  a = S; b = E
else:
  a = E; b = S

for i in range(a,b+1):
  print(i, end = " ")
