# 세 개의 정수를 입력받아 두 번째로 큰 수를 출력하는 프로그램을 작성하시오.

n = list(map(int,input().split()))

mid = sum(n) -( max(n) + min(n) )

print(mid)
