# 0이 입력되기 전까지 정수들을 계속 입력받아 그 개수와 합을 출력하시오.
# 0이 입력되기 전까지 여러 줄에 걸쳐 한 줄에 하나의 정수가 주어진다.
# 첫 줄에 개수를 출력하고, 다음 줄에 합을 출력한다 (자세한 형식은 출력 예를 참고한다).
# 단, 마지막 0은 계산에서 제외한다.

count = 0
total = 0

while True:
    n = int(input())
    if n == 0:
        break
    count += 1
    total += n

print('cnt =',count)
print('sum =',total)
