N = int(input())                         # 상자 개수
A = list(map(int, input().split()))      # 상자 안의 숫자들
K = int(input())                         # 한글이가 말한 숫자

for i in range(N):                       # 모든 상자 확인
    if A[i] == K:                        # 해당 상자의 숫자가 K와 같다면
        print(i + 1, end=' ')            # 상자 번호(1부터 시작)를 출력
