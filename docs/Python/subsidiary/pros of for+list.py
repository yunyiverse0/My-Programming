# for 반복문과 list 변수를 같이 썼을 때의 장점 



# 1. 반복해서 리스트 만들기 (append랑 같이)
squares = []
for i in range(1, 6):
    squares.append(i**2)   # 제곱한 값을 리스트에 추가
print(squares)



# 2. 조건 걸고 리스트 뽑아내기
nums = [1, 2, 3, 4, 5, 6]
odds = []
for n in nums:
    if n % 2 == 1:
        odds.append(n)   # 홀수만 리스트에 추가
print(odds)

