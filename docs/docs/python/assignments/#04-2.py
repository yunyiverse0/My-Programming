# 04 조건문 02

name = input("이름 : ")

kor, eng, mat = map(int,input().split())
tot = kor + eng + mat
avg = tot/3
# print(kor, eng, mat, tot, f"{avg:.2f}")

if avg >= 95:
  X = "A+"
elif avg >= 90:
  X = "A"
elif avg >= 85:
  X = "B+"
elif avg >= 80:
  X = "B"
elif avg >= 75:
  X = "C+"
elif avg >= 70:
  X = "C"
elif avg >= 65:
  X = "D+"
elif avg >= 60:
  X = "D"
elif avg <= 55:
  X = "F"
else:
  print("입력한 값을 다시 확인하세요.")

print(f"{name}님의 총점은{tot}점, 평균은 {avg:.2f}점, 학점은 {X} 학점 입니다.")
