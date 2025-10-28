#cmd 또는 VS code terminal에서 실행하는 코드들cmd 또는 VS code terminal에서 실행하는 코드들

# 1. 프로젝트 폴더 생성 및 이동
mkdir flask_login_project      #mkdri -> 폴더를 새로 만들어주는 명령어 (mkdri A : A라는 폴더를 새로 만들어줌)
cd flask_login_project         #cd -> 그 폴더로 이동한다 

# 2. 가상환경 생성 (venv는 가상환경 이름, 원하는 이름으로 변경 가능)
python -m venv venv            #이 프로젝트에서만 쓰는 파이썬 공간을 따로 만드는 것 (다른 프로젝트와의 충돌을 막아줌)

# 3. 가상환경 활성화
#    - Windows:
#      venv\Scripts\activate

# 4. Flask 설치 (가상환경이 활성화된 상태 즉 가상환경 안에 설치)
pip install Flask
