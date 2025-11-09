# 반복문을 사용하지 않고 N줄에 걸쳐 1부터 N까지 출력 예와 같이 출력하는 프로그램을 작성하시오.

def f(n):
    if n == 0:
        return
    f(n - 1)
    print('_' * n, n, sep='')

N = int(input())
f(N)
