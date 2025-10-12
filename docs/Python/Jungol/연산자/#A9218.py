# 두 개의 정수 N과 M을 입력받아서 N을 M으로 나눈 몫과 나머지를 곱한 값을 출력하는 프로그램을 작성하시오.

N, M = map(int,input().split())

print((N//M) *  (N % M))
