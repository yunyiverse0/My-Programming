###################클래스 밖에서 출력
# - 객체 생성해줘야함 >> class를 만든 건 설게도만 만든거라 실제로 사용할 물건, 즉, 객체를 만들어줘야 실행 가능
# -클래스 안 사용자 정의 함수에 입력받은 변수 넣어줘야함

class j:
    def f(self, loc, bed, bat):
        self.loc = loc
        self.bed = bed
        self.bat = bat

J = j()    #객체 생성
Loc, Bed, Bat = input().split()
J.f(Loc, Bed, Bat)    #함수에 변수 대

print('location:',J.loc)
print('bedrooms:',J.bed)
print('bathrooms:',J.bat)

#####################클래스 안에 출력 기능 넣기
# 실제 회사 코드에선  __init__에 변수저장, 기본값설정, 객체준비 정도로만 씀 (정올은 연습용 코드이기에 괜찮음) >> 객체를 만들었는데 갑자기 출력되는 게 실제에선 위험이 있음

class J:
    def __init__(self):
        self.loc, self.bed, self.bat = input().split()
        
        print("location:", self.loc)
        print("bedrooms:", self.bed)
        print("bathrooms:", self.bat)

house = J()
