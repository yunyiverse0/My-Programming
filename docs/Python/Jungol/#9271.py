# 정수 S와 정수 E를 입력받아 정수 S부터 정수 E까지의 모든 홀수를 출력하는 프로그램을 작성하시오. 
# (S와 E는 홀수이며, S는 E보다 작거나 같음이 보장된다.)

# 방법1
S, E = map(int, input("2개의 홀수를 입력하세요: ").split())

for i in range(S, E+1, 2):
    print(i)

# if S와 E가 홀수라는 조건이 주워지지 않았을 때

# 방법 1

S, E = map(int, input("2개의 홀수를 입력하세요: ").split())

if S % 2 == 0: 
    S += 1      # S가 짝수이면 1을 더해서 홀수로 만든다

for i in range(S, E+1, 2):
    print(i)

# 방법2

S, E = map(int, input("2개의 홀수를 입력하세요: ").split())

for i in range(S, E+1):
    if i % 2 == 1:      # 조건문으로 i 나누가 2의 몫이 1일 때만 출력이 되도록 설정
        print(i)
