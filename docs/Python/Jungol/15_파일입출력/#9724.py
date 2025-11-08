# 두 정수와 한 개의 연산자(+, -, *, /, %)를 입력받아 계산식을 출력하는 프로그램을 작성하시오.

# 마지막에 연산자가 들어있으니까 리스트[2] = 연산자

with open("input.txt",'r') as f, open("output.txt","w+") as F:
    flist = [i for i in f.readline().split()]
    
    x = int(flist[0]); y = int(flist[1])

    if flist[2] == '+':
        A = x + y
    elif flist[2] == '-':
        A = x - y
    elif flist[2] == '*':
        A = x * y
    elif flist[2] == '/':
        A = x / y
    else:
        A = x % y

    F.write(f"{flist[0]} {flist[2]} {flist[1]} = "+str(A))
