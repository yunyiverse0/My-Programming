# 이상 10이하의 정수 N이 주어졌을 때, 1부터 3까지의 정수를 중복을 허용하여 N번 나열하는 모든 경우를 출력하는 프로그램을 작성하시오.

n = int(input())

def f(x, y):
    if x == n:
        print(*y)
        return        #여기서 끝내라는 뜻
    
    for i in range(1, 4):
        y.append(i)
        f(x + 1, y)        #f(x+1,y)가 if조건에 걸려서 멈추기 전까지는 pop이 실행되지 않음
        y.pop()

f(0, [])
