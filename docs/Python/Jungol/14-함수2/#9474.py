# 두 개의 정수를 입력받아 절댓값이 큰 수를 출력하고, 두 개의 실수를 입력받아 절댓값이 작은 수를 출력하는 프로그램을 작성하시오.

a, b = map(int,input().split())

if abs(a) > abs(b):
    A = a
else:
    A = b

c, d = map(float,input().split())

if abs(c) < abs(d):
    B = c
else:
    B = d

print(A)
print(B)

######GPT가 짜준 코드 

a, b = map(int, input().split())
A = max(a, b, key=abs)

c, d = map(float, input().split())
B = min(c, d, key=abs)

print(A)
print(B)
