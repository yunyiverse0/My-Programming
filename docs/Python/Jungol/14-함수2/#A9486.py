# 첫 줄에 세 개의 전구의 상태가 주어진다. 각 전구가 켜져 있으면 1 아니면 0으로 표시된다.
# 두 번째 줄에 정수 K가 주어진다.
# 전구를 끄거나 켜서 K개의 전구가 켜져있는 상태를 만들기 위해 최소 몇 개의 전구를 끄거나 켜야하는지 출력하는 프로그램을 작성하시오.

jg = list(map(int,input().split()))
K = int(input())


if jg.count(1) == K:
    print(0)
elif jg.count(1) > K:
    print(jg.count(1) - K)
else:
    print(K - jg.count(1))

