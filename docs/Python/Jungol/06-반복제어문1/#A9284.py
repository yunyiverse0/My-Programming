N = int(input())

A = 2 - N % 2     
for i in range(A, N + 1, 2):
    print(i, end=" ")

# A 짝수 2 - 0(짝수 % 2 = 0) = 2
# A 홀수 2 - 1(홀수 % 2 = 1) = 1
