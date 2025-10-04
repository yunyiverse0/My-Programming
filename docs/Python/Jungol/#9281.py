i = 0

while True:
    N = int(input())
    if N == 0:        # 0이면 종료
        break
    if N <= 0:        # 음수이거나 0 이면 더하지 않고 건너뜀
        continue
    i += N            # 양수만 더함

print(i) 
