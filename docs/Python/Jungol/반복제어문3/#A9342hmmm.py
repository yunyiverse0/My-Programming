# 정수 N을 입력받아서 출력예와 같이 출력하는 프로그램을 작성하시오.

# N = 5

#     *
#   ***
# *****
#   ***
#     *


n = int(input())  
m = (n + 1) // 2  

for i in range(1, n + 1):
    k = abs(m - i)
    print("  " * k + "*" * (n - 2 * k)
