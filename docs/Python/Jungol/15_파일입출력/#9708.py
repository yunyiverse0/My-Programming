# input.txt" 파일로부터 이름과 국어, 영어점수를 입력받아 이름과 합계, 평균을 화면과 "output.txt" 파일에 출력하는 프로그램을 작성하시오.

#with문 쓰려면 아래 종속절을 들여써야함
#with문 사용 후 콜론 적어야함
with open("input.txt","r") as f:
    score = f.readline().split()

hap = int(score[1]) + int(score[2])
avg = hap / 2

with open ("output.txt","w") as F:    #쓰기 모드에선 쓰기만 가능해서 읽기 쓰기 모드로 한 번에 해야 출력이 가능
    F.write(f"{score[0]} {hap} {avg:.1f}")
    print(F.read())    #파일 객체 자체를 print하는 건 안되기에 read써줘야함
