# 정수 N을 입력받아서 출력예와 같이 출력하는 프로그램을 작성하시오.

# N = 5

# *
# **
# ***
# **
# *

N = int(input())

for i in range(N):
    if i <= N //2:
        print((i+1)*'*')
    else:
        print((N-i)*'*')

