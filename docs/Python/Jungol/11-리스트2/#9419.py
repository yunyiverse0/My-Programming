rows = []
rows.append([1, 1, 1, 1, 1])     # 1번째 줄
rows.append([1, 2, 3, 4, 5])     # 2번째 줄

# 3번째 ~ 5번째 줄: 직전 줄의 누적합
for _ in range(3):
    prev = rows[-1]
    s = 0
    curr = []
    for v in prev:
        s += v
        curr.append(s)
    rows.append(curr)

# 출력
for r in rows:
    print(*r)
