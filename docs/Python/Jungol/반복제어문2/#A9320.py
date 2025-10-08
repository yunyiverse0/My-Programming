# 한 개의 정수를 입력받아 그 수의 배수를 차례로 10개 출력하는 프로그램을 작성하시오.

N = int(input())

for i in range(1,11):
  a = N*i
  print(a , end = " ")
