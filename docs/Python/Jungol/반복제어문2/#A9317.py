# 정수를 입력받아서 1부터 입력받은 정수까지의 5의 배수를 첫 행에 출력하고 마지막 행에는 그 수들의 합을 출력하는 프로그램을 작성하시오.

N = int(input())
sum = 0

for i in range(5,N+1,5):
  print(i,end = " ")
  sum += i
print()
print(sum)
