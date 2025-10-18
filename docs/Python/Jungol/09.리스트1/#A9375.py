# 연속 증가 리스트는 연속된 원소가 모두 증가하는 순서로 되어 있는 리스트를 의미한다. 즉, 각 원소는 연속 증가 리스트 내의 해당 원소보다 왼쪽에 있는 모든 원소보다 크다.
# 주어진 길이 N의 리스트가 연속 증가 리스트라면 YES를, 아니라면 NO를 출력하는 프로그램을 작성하시오.

N = int(input())
A = []

for i in range(N):
  n = int(input())
  A.append(n)

a = "YES"

for j in range(1,N):
  if A[j-1] > A[j]:
    a = "NO"
    break

print(a)
