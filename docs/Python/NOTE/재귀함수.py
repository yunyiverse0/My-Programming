#재귀함수는 함수를 정의한 후, 함수 내에서 자신을 다시 호출하여 작업을 수행하는 방식의 함수

def f(N):
  if N == 1:
    return 1
  else:
    return (N*f(N-1))

n = int(input())
result = f(n)
print(result)

f(5) = 5 * f(4) >>> ?
f(4) = 4 * f(3) >>> ?
f(3) = 3 * f(2) >>> ?
f(2) = 2 * f(1) >>> ?
f(1) = return 1 >>> 종료
