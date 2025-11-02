# 세 개의 문자열을 입력받아 각각의 길이가 순서대로 저장된 리스트를 만들어 출력하는 프로그램을 작성하시오

STR = input().split()

num = []

for i in STR:
    x = len(i)
    num.append(x)

print(num)
