# 열 개의 실수를 입력받아 반올림한 정수의 값이 원래의 값보다 커지는 수들의 개수를 출력하는 프로그램을 작성하시오

nums = list(map(float,input().split()))
 
total = 0 

for i in nums:
    if round(i) > i:
        total += 1

print(total)
