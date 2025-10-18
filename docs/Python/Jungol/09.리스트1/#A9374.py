# 100개 이하의 정수를 계속 입력받다가 0이 입력되면 0을 제외하고 그때까지 입력된 정수 중
# 홀수는 odd리스트에 짝수는 even리스트에 저장하여 다음과 같이 출력하는 프로그램을 작성하시오.

odd = []; even = []

for i in range(100):
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print('odd =',odd,'\neven =',even)
