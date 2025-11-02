# 원의 반지름에 해당하는 실수를 입력받아 원의 넓이의 버림, 올림, 반올림을 각각 구하는 프로그램을 작성하시오.

import math

r = float(input())
w  = (r ** 2) * 3.14

print(f'''원의 넓이
버림 : {math.floor(w)}
올림 : {math.ceil(w)}
반올림 : {round(w)}''')
