# 한 줄에 여러 개의 정수를 입력받아 3의 배수이면서 5의 배수인 정수를 입력된 순서대로 모두 출력하고 다음 줄에 그 개수를 출력하는 프로그램을 작성하시오. 
# 한 개도 없을 경우에는 첫 줄에 "0"만 출력한다. 입력되는 정수의 최대 개수는 1000개이다

with open("input.txt", "r") as f, open("output.txt","w+") as F:
    a = [int(i) for i in f.readline().split()]
    A = []
    for i in a:
        if i % 3 == 0 and i % 5 == 0:
            A.append(i)

    if len(A) == 0:
        A.append(0)

    for i in range(len(A)):
        if i == len(A):
            F.write(str(A[i]))
        else:
            F.write(str(A[i])+' ')
    
    F.write(f'\n{len(A)}')
