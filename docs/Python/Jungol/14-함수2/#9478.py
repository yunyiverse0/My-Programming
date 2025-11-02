# 문자열 리스트 A를 입력받아 map 함수를 이용하여 각 문자열을 문자 리스트로 변환하여 저장한 후 리스트를 출력하는 프로그램을 작성하시오.

A = input().split()    
B = list(map(list, A))   
print(B)
