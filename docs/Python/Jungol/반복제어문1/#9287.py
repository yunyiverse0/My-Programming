# 두 정수를 입력받아 입력받은 두 정수 사이의 모든 짝수들의 합을 출력하는 프로그램을 작성하시오. 
# 첫 번째 수가 두 번째 수보다 작거나 같음이 보장된다.

a, b = map(int,input().split())

total = 0
c = 2

if a % 2 != 0:
  a = a + 1

for i in range(a, b+1, c):
  total = total + i
print(total)
