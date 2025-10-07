# 정수 N을 입력받아 N단 구구단을 출력하는 프로그램을 작성하시오.

N = int(input())

for i in range(1,10):
    for _ in range(N,N+1):
        print(f"{N} * {i} = {N*i}")
