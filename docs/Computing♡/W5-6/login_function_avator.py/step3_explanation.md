```python
import json  # <sub>JSON 파일을 다루는 내장 모듈. users.json 파일을 읽기 위해 사용.</sub>
from flask import Flask, render_template, request, redirect, url_for, session, flash  # <sub>Flask 모듈에서 필요한 기능만 가져옴 (서버, HTML 렌더링, 요청/응답, 세션, 메시지 등)</sub>

app = Flask(__name__)  # <sub>Flask 애플리케이션(서버) 생성. __name__은 현재 파일 이름을 의미하며 Flask가 경로를 인식할 때 사용.</sub>
app.secret_key = 'yunyi'  # <sub>flash 메시지와 session을 보호하기 위한 보안 키 (임의 문자열).</sub>

def load_users():  # <sub>JSON 파일(users.json)을 열어 파이썬 dict로 변환하는 함수.</sub>
    with open('users.json', 'r', encoding='utf-8') as f:
        return json.load(f)  # <sub>json.load() → JSON 데이터를 딕셔너리로 읽어옴.</sub>

@app.route('/')  # <sub>루트('/') 주소로 들어왔을 때 동작하는 경로 설정.</sub>
def index():
    return redirect('login')  # <sub>메인 페이지 접근 시 /login으로 강제 이동.</sub>

@app.route('/login', methods=['GET', 'POST'])  # <sub>로그인 페이지 라우트. GET(보여주기)와 POST(보내기) 방식 모두 허용.</sub>
def login():
    data = load_users()  # <sub>users.json에서 유저 정보를 불러옴.</sub>
    if request.method == 'POST':  # <sub>POST 방식일 경우 (폼 제출 시)</sub>
        username = request.form['username']  # <sub>폼에서 입력받은 아이디를 가져옴.</sub>
        password = request.form['password']  # <sub>폼에서 입력받은 비밀번호를 가져옴.</sub>

        if username in data and data[username]['password'] == password:  # <sub>아이디와 비밀번호가 모두 일치할 때</sub>
            flash('Login was successful.')  # <sub>로그인 성공 메시지 잠깐 표시.</sub>
            session['username'] = username  # <sub>세션에 로그인한 사용자 이름 저장.</sub>
            return redirect(url_for('welcome'))  # <sub>/welcome 페이지로 이동.</sub>

        elif username in data and data[username]['password'] != password:  # <sub>아이디는 맞지만 비밀번호가 틀린 경우</sub>
            flash('The user password is incorrect.')  # <sub>비밀번호 오류 메시지 표시.</sub>
            return render_template('login.html')  # <sub>로그인 페이지 다시 보여줌.</sub>

        elif username not in data and any(user['password'] == password for user in data.values()):  # <sub>아이디가 존재하지 않는데 입력한 비밀번호가 누군가의 비밀번호와 일치하는 경우</sub>
            flash('The username is incorrect')  # <sub>아이디 오류 메시지.</sub>
            return render_template('login.html')

        else:  # <sub>아이디와 비밀번호 둘 다 틀릴 때</sub>
            flash('Both username and password are incorrect')  # <sub>전체 오류 메시지.</sub>
            return render_template('login.html')

    return render_template('login.html')  # <sub>GET 요청일 때 로그인 페이지 보여줌.</sub>

@app.route('/welcome')  # <sub>로그인 성공 시 이동하는 페이지 경로.</sub>
def welcome():
    username = session.get('username')  # <sub>세션에서 로그인한 사용자 이름 꺼냄.</sub>
    return render_template('welcome.html', username=username)  # <sub>welcome.html 파일에 사용자 이름 전달해 렌더링.</sub>

@app.route('/logout')  # <sub>로그아웃 경로.</sub>
def logout():
    return redirect(url_for('login'))  # <sub>로그아웃 시 로그인 페이지로 이동. (실제 서비스에선 session.clear() 권장)</sub>

if __name__ == '__main__':  # <sub>이 파일이 직접 실행될 때만 서버를 실행.</sub>
    app.run(debug=True)  # <sub>Flask 서버 실행. debug=True면 코드 변경 시 자동 재시작.</sub>
