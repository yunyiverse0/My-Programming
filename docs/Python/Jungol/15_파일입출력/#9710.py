# 현재 프로젝트 폴더의 하위에 "temp" 폴더를 생성하고 "temp"폴더의 "in.txt" 파일로부터 10개의 정수를 입력받아 짝수 번째 입력받은 정수를 "temp" 폴더의 "out.txt" 파일에 출력하는 프로그램을 작성하시오.

with open("in.txt","r") as In:
    n = In.readline().split()

A = [n[i] for i in range(len(n)) if i % 2 == 1]


with open("out.txt","w+") as Out:
    for i in A:
        Out.write(str(i)+' ')
    Out.seek(0)
    print(Out.read())
