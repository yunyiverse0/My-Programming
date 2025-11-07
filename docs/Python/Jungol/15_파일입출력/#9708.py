# input.txt" 파일로부터 이름과 국어, 영어점수를 입력받아 이름과 합계, 평균을 화면과 "output.txt" 파일에 출력하는 프로그램을 작성하시오.

#with문 쓰려면 아래 종속절을 들여써야함
#with문 사용 후 콜론 적어야함
with open("input.txt","r") as f:
    score = f.readline().split()

hap = int(score[1]) + int(score[2])
avg = hap / 2

with open ("output.txt","w") as f:    #쓰기 모드에선 쓰기만 가능해서 읽기 쓰기 모드로 한 번에 해야 출력이 가능
    f.write(f"{score[0]} {hap} {avg:.1f}")
    f.seek(0)            #원래라면 f.read만 했을 땐 실행이 안됨 -> 커서(포인터)가 끝에 가 있기에 read(커서 위치~끝 까지 출력하는 함수)함수는 빈 문자열을 반환해줌 따라서 커서 위치를 변경시켜줘야함
    print(f.read())    #파일 객체 자체를 print하는 건 안되기에 read써줘야함
