# 정수 N을 입력받아 1부터 4까지의 모든 정수들 중 정수 N을 제외한 수들을 출력하는 프로그램을 작성하시오. 단, continue를 사용한다.

N = int(input())       # N을 while문 안에 넣으면 입력을 계속해서 받게 됨
i = 1                  # 시작값

while i <= 4:          # 시작값은 정했으니 끝나는 값만 정해주면 됨
    if i == N:
        i += 1         # i = i + 1 도 가능하긴 하지만 i += 1이 더 간단, continue 후에 쓰면 i를 건너뛰어버림
        continue
    print(i)
    i += 1             
