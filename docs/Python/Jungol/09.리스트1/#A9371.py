# 첫 번째 줄에 두 개의 정수 a, b를 입력받아, a가 b개인 리스트를 만들고, 
# 두 번째 줄에도 같은 작업을 반복하여 새로운 리스트를 만든 후, 두 리스트를 합하여 출력 예와 같이 출력하는 프로그램을 작성하시오.

a, b = map(int,input().split())
c, d = map(int,input().split())

A = [a, b]; B = [c, d]; C = []

for i in range(b):
    C.append(a)
for i in range(d):
    C.append(c)

print(C)
