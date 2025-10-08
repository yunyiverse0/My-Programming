# 정수를 입력받아 다음과 같이 순서쌍을 출력하는 프로그램을 작성하시오.

N = int(input())
a = 1

for i in range(1,N+1):
    for j in range(1,N+1):
        print(f"({i}, {a})", end = " ")
        a += 1
    a = 1        # a값 초기화
    print()
