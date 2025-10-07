# 출력 예와 같이 3 x 3 크기의 행렬를 두 번 출력하는 프로그램을 작성하시오.

for i in range(1):
    for j in range(1, 4):
        print(f"{j} {j} {j}")
    print()
for i in range(3):
    for j in range(1,4):
      print(j, end=" ")
    print()
