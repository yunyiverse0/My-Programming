i = 0
N = -1   # 처음에 0이 아닌 값으로 시작

while N != 0:          # 0이 들어오기 전까지만 반복
    N = int(input())
    if N <= 0:         # 음수나 0은 건너뛰기
        continue
    i += N             # 양수만 더하기

print(i)               # ← while문 끝나고 최종 합 출력

