# 첫 번째 줄에 국어 점수가 주어진다.
# 두 번째 줄에 영어 점수가 주어진다.
# 세 번째 줄에 수학 점수가 주어진다.
# 네 번째 줄에 정보 점수가 주어진다.

# tot: 353
# avg: 88

kor = int(input())
eng = int(input())
mat = int(input())
inf = int(input())

tot = kor + eng + mat + inf

print(f"tot: {tot} \navg: {int(tot/4)}")
