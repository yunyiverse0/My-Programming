# "done"이 입력되기 전까지 계속 명령어와 여러 개의 정수를 한 줄로 입력받아 명령어가 int라면 정수 리스트에 저장하고,
# 명령어가 float라면 정수들을 float로 형 변환시킨 값들을 리스트에 저장하여 리스트를 출력하는 프로그램을 작성하시오.

while True:
    A = input().split()
    INT = []
    FLOAT = []
    if A[0] == 'int':
        INT.extend(map(int, A[1:]))
        print(INT)
    elif A[0] == 'float':
        FLOAT.extend(map(float, A[1:]))
        print(FLOAT)
    else:
        break
