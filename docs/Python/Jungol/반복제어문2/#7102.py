# 정수 N을 입력받은 후, 다음 줄부터 N개의 정수를 입력받아 홀수의 합계와 짝수의 개수를 출력하는 프로그램을 작성하시오.

N = int(input(""))
a = 0
sum = 0
num1 = []
num2 = []

while N > len(num2):
  a = int(input())
  num2.append(a)
  if a % 2 == 1:
    sum += a
  else:
    num1.append(a)
print(sum,len(num1))
