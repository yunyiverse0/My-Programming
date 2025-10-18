# 100개 이하의 정수를 계속 입력받다가 0이 입력되면 0을 제외하고 그때까지 입력된 정수 중 5의 배수들의 리스트를 출력하고 리
# 스트에 있는 원소들의 개수, 합계, 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수 첫째자리까지 출력한다.

A = []

for i in range(100):
    n = int(input())
    if n == 0:
        break
    if n % 5 == 0:
        A.append(n)
print(A,'\nCNT:',len(A),"\nHAP:",sum(A),'\nAVG:',sum(A)/len(A))
