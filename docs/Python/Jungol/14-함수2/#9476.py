# 세 개의 실수를 입력받아
# 가장 큰 수를 올림한 정수를 출력하고
# 가장 작은 수를 버림한 정수를 출력한 후
# 남은 수를 반올림한 정수를 출력하는 프로그램을 작성하시오.

import math

a = list(map(float,input().split()))
n = sum(a) -( max(a) + min(a))

print(math.ceil(max(a)),math.floor(min(a)),round(n))
