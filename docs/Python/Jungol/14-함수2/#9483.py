# 2원짜리 동전 A개, 3원짜리 동전 B개를 이용하여 정확하게 C원을 만들 수 있는지 확인하는 프로그램을 작성하시오.
# 첫 번째 줄에 테스트 케이스의 수 T를 입력받는다.
# 다음 줄부터 T번에 걸쳐 정수 A, B, C를 입력받아 정확하게 C원을 만드는 것이 가능하면 "YES", 안되면 "NO"를 출력한다.

T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    possible = False

    for i in range(A + 1):      
        for j in range(B + 1):   
            if 2*i + 3*j == C:
                possible = True

    print("YES" if possible else "NO")    # possible = True일 때만 실행
