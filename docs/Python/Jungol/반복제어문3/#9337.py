N = int(input())
a = ord('A')

for i in range(1,N+1):
    for j in range(i):           # 각 행마다 i개씩 알파벳 출력
        print(chr(a), end='')    # 아스키코드 → 문자로 바꿔서 출력
        a += 1                   # 다음 알파벳으로 이동
    print() 
