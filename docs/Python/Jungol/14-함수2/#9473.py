# -100과 100 사이의 열 개의 정수를 입력받아 절댓값의 합을 구해 출력하는 프로그램을 작성하시오

n = list(map(int,input().split()))
N = [abs(i) for i in n]

print(sum(N))
