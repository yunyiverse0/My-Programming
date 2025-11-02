# 번부터 N번까지 번호가 매겨진 달걀들이 일렬로 나열되어 있다. 정수 N과 두 정수 a, b를 입력받아 a번 달걀과 b번 달걀의 위치를 바꾼 후 출력하는 프로그램을 작성하시오

N = int(input())
a, b = map(int,input().split())
nums = []

for i in range(N+1):
  nums.append(i)

if nums[a] > nums[b]:
  nums[b], nums[a] = nums[a], nums[b]
else:
  nums[a], nums[b] = nums[b], nums[a]

print(*nums)
