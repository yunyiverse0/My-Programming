# 두 개의 정수를 입력받아 작은 수부터 큰 수까지 3의 배수이거나 5의 배수인 수들의 개수와 합 을 출력하는 프로그램을 작성하시오.

a, b = map(int,input().split())
sum = 0
SUM = []

if a < b:
    for i in range(a, b+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            SUM.append(i)
else:
    for i in range(b, a+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            SUM.append(i)
print(f"""CNT: {len(SUM)}
SUM: {sum}""")
