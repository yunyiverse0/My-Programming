# 정수 N을 입력받아 N단 구구단을 세 줄에 걸쳐 출력하는 프로그램을 작성하시오. 
# 각 식 사이의 간격은 공백 세 개로 정한다.

# 방법1 - 머리가 나쁘면 몸이 고생한
N = int(input())
a = 1

for _ in range(1):
  for i in range(1,4):
      print(f"{N} * {a} = {N*i}",end="   ")
      a+=1
  print()
  for i in range(4,7):
      print(f"{N} * {a} = {N*i}",end="   ")
      a += 1
  print()
  for i in range(7,10):
      print(f"{N} * {a} = {N*i}",end="   ")
      a+=1
  print()
# 방법 2 - 나는 감히 생각도 못할 지피티가 짜준 코드
N = int(input())

for i in range(0, 9, 3):             # 0, 3, 6 → 세 줄 나누는 기준
    for j in range(1, 4):            # 각 줄에 3개씩 출력
        a = i + j                    # i = 0, j = 1 ...
        print(f"{N} * {a} = {N*a}", end="   ")
    print()                          # 한 줄 끝나면 줄바꿈
