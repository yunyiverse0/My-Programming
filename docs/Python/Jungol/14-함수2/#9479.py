인자로 받은 과일들의 이름을 출력하는 함수를 작성하시오.

def f(*ars):
  for i in range(1, len(N)+1):
    print(*N[:i])
N = ['apple','banana','coconut']
f(N)
