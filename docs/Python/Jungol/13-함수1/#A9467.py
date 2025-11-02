# 두 정수 A와 B를 받아 A+B의 절대값을 반환하는 함수를 호출하여 그 결과를 출력하는 프로그램을 작성하시오

def f():
  A, B = map(int,input().split())
  j = abs(A+B)
  print(j)

f()
