# 자연수 N을 입력받아 출력예와 같이 N행 N열의 숫자사각형을 출력하는 프로그램을 작성하시오.

# (출력하는 부분은 함수로 작성한다.)

N = int(input())

def f():
    n = 1
    for i in range(N):
        for j in range(N):
            print(n, end = ' ')
            n += 1    
        print()

f()
