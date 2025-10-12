# N = 3

#     1
#   1 2
# 1 2 3

N = int(input())

for i in range(1, N + 1):
    if N == 1:                    # N이 1일 땐 공백 없이 바로 출력
        print(1)
    else:
        print('  ' * (N - i), end='')   # 오른쪽 정렬 (공백 2칸씩)
        for j in range(1, i + 1):
            print(j, end='')
        print()
