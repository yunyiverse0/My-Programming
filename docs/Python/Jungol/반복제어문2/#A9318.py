# 정수 N을 입력받고 이어서 N개의 점수를 입력받아 합과 평균(몫)을 출력하는 프로그램을 작성하시오

N = int(input())
sum = 0

for i in range(N):
    score = int(input())
    sum += score 
print(f"""SUM: {sum}
AVG: {int(sum/N)}""")
