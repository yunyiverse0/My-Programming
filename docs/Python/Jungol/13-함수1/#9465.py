# 1부터 전달받은 수까지의 합을 출력하는 함수를 작성하고 1000 이하의 자연수를 입력받아 작성한 함수로 전달하여 출력하는 프로그램을 작성하시오.

def f():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

sum = f()

print(sum)
