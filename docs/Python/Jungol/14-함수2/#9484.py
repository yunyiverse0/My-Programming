# 여덟 개의 정수를 한 줄에 입력받아 리스트에 저장하고, 최댓값에 해당하는 값이 저장된 인덱스를 모두 출력하는 프로그램을 작성하시오.
# (hint: 최댓값을 구하는 함수와 인덱스를 출력하는 함수를 각각 만들어서 구조화를 한다

def f1(nums):
    return max(nums)    #최댓값 반환하는 함수

def f2(nums):
    Max = f1(nums)
    for i in range(len(nums)):
        if nums[i] == Max:      #인덱스 i의 원소가 최댓값이면 인덱스 i 출력
            print(i, end=' ')

A = list(map(float, input().split()))
f2(A)
