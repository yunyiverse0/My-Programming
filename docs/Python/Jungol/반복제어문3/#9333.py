N = int(input())

for i in range(N):
    if i <= N // 2:      #i의 절반 이하는 별을 줄여라
        print("  " * (2 * i) + "* " * (N - 2 * i))
    else:
        print("  " * (2 * (N - i - 1)) + "* " * (2 * (i - N // 2) + 1))

# N//2+1 가운데 줄 보다 한 줄 아래
