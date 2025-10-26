# 학생들의 점수를 입력받아서 점수를 10점 단위로 구분하여 점수대 별 학생 수를 출력하는 프로그램을 작성하시오
# 첫 줄에 학생들의 점수 다섯 개가 공백으로 나누어 주어진다.

a = map(int,input().split())
A = []
for i in a:
    n = (i // 10)
    A.append(n*10)

for i in range(100,-1,-10):
    if A.count(i) >= 1:
        print(f"{i}: {A.count(i)} person")
