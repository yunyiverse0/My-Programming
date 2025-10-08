# 행과 열의 수를 입력받아 다음과 같이 출력하는 프로그램을 작성하시오.

a, b = map(int,input().split())

for i in range(1, a+1):
  for j in range(1,b+1):
    print(i*j, end= " ")      # 각 열에 나열된 숫자 * 행
  print()

# 뭔가 점점 코드만 생각해내야하는 게 아닌 수학적인 것도 잘 풀어봐야하는 느낌이네요..클낫
