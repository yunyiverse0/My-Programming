# 행 5열 2차원 문자리스트에 차례로 대문자를 입력받은 후 소문자로 바꾸어서 출력하는 프로그램을 작성하시오

a = [input().split() for _ in range(3)]

for i in a:
    for j in i:
        print(j.lower(), end=' ')
    print()
