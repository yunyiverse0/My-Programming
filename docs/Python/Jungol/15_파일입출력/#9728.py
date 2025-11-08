# 3000 이하의 정수로 된 시작 연도와 끝 연도를 입력받아 윤년이 몇 번인지를 구하여 출력하는 프로그램을 작성하시오.

with open("input.txt","r") as f, open("output.txt","w+") as F:
    a = [int(i) for i in f.readline().split()]
    A = []
    x = a[0]; y = a[1]

    for i in range(x, y+1):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            A.append(i)

    F.write(str(len(A)))
