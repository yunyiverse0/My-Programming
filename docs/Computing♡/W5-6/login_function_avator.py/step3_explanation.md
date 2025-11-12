## Flask 로그인 코드 해설 노트

---

\```python
import json
from flask import Flask, render_template, request, redirect, url_for, session, flash
\```
Flask와 json 모듈을 불러옴.  
- `json` : 파일에서 데이터를 읽고 쓰는 내장 모듈  
- `Flask` : 웹 애플리케이션 생성  
- `render_template` : HTML 파일 렌더링  
- `request` : 클라이언트의 요청 데이터 처리  
- `redirect`, `url_for` : 페이지 이동  
- `session` : 로그인 상태 유지  
- `flash` : 1회용 알림 메시지 표시  

---

\```python
app = Flask(__name__)
app.secret_key = 'yunyi'
\```
Flask 앱(서버)을 생성하고 flash, session 보안키를 설정함.  

---

\```python
def load_users():
    with open('users.json', 'r', encoding='utf-8') as f:
        return json.load(f)
\```
users.json 파일을 열어 Python의 dict 형태로 변환하는 함수.  

---

\```python
@app.route('/')
def index():
    return redirect('login')
\```
루트('/') 접근 시 /login으로 이동.  

---

\```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    data = load_users()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in data and data[username]['password'] == password:
            flash('Login was successful.')
            session['username'] = username
            return redirect(url_for('welcome'))

        elif username in data and data[username]['password'] != password:
            flash('The user password is incorrect.')
            return render_template('login.html')

        elif username not in data and any(user['password'] == password for user in data.values()):
            flash('The username is incorrect')
            return render_template('login.html')

        else:
            flash('Both username and password are incorrect')
            return render_template('login.html')

    return render_template('login.html')
\```
- GET → 로그인 페이지 표시  
- POST → 입력값을 받아 검증 후 메시지 출력 및 페이지 이동  

---

\```python
@app.route('/welcome')
def welcome():
    username = session.get('username')
    return render_template('welcome.html', username=username)
\```
세션에 저장된 username을 가져와 welcome.html로 전달.  

---

\```python
@app.route('/logout')
def logout():
    return redirect(url_for('login'))
\```
로그아웃 시 로그인 페이지로 이동.  
(실제 서비스에서는 `session.clear()`로 세션 삭제 권장)  

---

\```python
if __name__ == '__main__':
    app.run(debug=True)
\```
Flask 서버 실행.  
debug=True → 코드 변경 시 자동 재시작.  
---

✅ 위 내용을 그대로 복사해서 깃허브 `.md` 파일에 붙이면  
“코드가 상자처럼 표시 + 설명은 아래에 노트처럼 표시”돼.  

(\``` ← 백틱 세 개는 실제로는 역슬래시 없이 써야 돼,  
여기선 복사 시 깨지지 않게 역슬래시로 표시한 거야.)
