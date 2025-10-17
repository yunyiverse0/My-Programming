# 최대 100개의 정수를 차례로 입력받다가 -1이 입력되면 입력을 중단하고 -1을 제외한 마지막 세 개의 정수를 출력하는 프로그램을 작성하시오.(입력받은 정수가 3개 미만일 경우에는 모두 출력한다.)

# 내가 짠 코드
A = []

for i in range(100):
    n = int(input())
    A.append(n)
    if n == -1:
        A.remove(-1)
        if len(A) < 3:
            for j in A:
                print(j,end = ' ')
        else:
            a = A[len(A)-3:]
            for j in a:
                print(j, end =' ')
        break

  # 지피티가 피드백한 코드
  A = []

while True:        #언제까지 입력받을지 모를 때는 while사용이 용이 (근데 이 문제는 최대 100까지 입력 받으라 했으니 for문이 낫지않을까요?)
    n = int(input())
    if n == -1:
        break
    A.append(n)    #-1을 자동으로 A리스트에서 배제해줌

if len(A) < 3:
    result = A
else:
    result = A[-3:]    #굳이 변수를 따로 안세워도 됨. slicing문법은 복제해서 new list를 만들기에 이런 게 간ㅇ

for j in result:
    print(j, end=' ')
