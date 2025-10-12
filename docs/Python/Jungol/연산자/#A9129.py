# 사각형의 가로, 세로 길이를 입력받아 가로 길이는 2배하고, 세로 길이는 3 감소시켜서 저장한 후 가로, 세로, 넓이를 차례로 출력하는 프로그램을 작성하시오.

a = int(input())
b = int(input())

a = a * 2
b = b - 3

print(f'''width = {a}
length = {b}
area = {a*b}''')
