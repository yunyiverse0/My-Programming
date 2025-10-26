n = int(input())

a = [[0]*n for _ in range(n)]  # n×n 2차원 리스트 생성

# 파스칼 삼각형 값 채우기
for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:   # 양 끝은 1
            a[i][j] = 1
        else:
            a[i][j] = a[i-1][j-1] + a[i-1][j]

# 마지막 행부터 위로 출력
for i in range(n-1, -1, -1):
    for j in range(i+1):
        print(a[i][j], end=' ')
    print()
