# 수 n (n≤10)을 입력받아 n!을 구하여 출력하는 프로그램을 작성하시오

with open("input.txt","r") as f, open("output.txt", "w+") as F:
    A = f.readline()
    n = 1
    a = int(A)
    for i in range(1, int(A)):
        a *= i

    F.write(str(a))
