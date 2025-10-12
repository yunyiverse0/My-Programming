# 한 줄에 영문 알파벳 소문자 a부터 z까지 출력하는 프로그램을 작성하시오.

for i in range(ord('a'),ord('z')+1,1):
    print(chr(i), end = ' ')
