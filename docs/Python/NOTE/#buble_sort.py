n = int(input())
A = list(map(int, input().split()))

for i in range(n - 1):      # n-1개가 정렬 되었을 땐 가장 큰 원소 1개만 남으니 굳이 N개까지 정렬할 필요가 X
    for j in range(n - 1 - i):  # i = n-1 / n - i - 1 개 정리
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
    print(A)
