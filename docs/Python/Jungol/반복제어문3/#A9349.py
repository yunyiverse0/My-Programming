# 정수 N을 입력받아 알파벳 중 N의 배수 번째 알파벳만 출력하는 프로그램을 작성하시오.
# 1<=N<=26

N = int(input())
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(N, 27, N):        
    print(alphabet[i-1], end='')    #인덱스는 0부터 시작하는데 i는 1부터 시작이라 시작점 맞
