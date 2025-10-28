# flask app 생성

# 1.프로젝트 폴더 안에 app.py 폴더 생성 후 폴터에 코드 넣음

import json
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

# 나중에 사용자 정보 등을 .json 파일에 저장할 때 사용
def load_users():
    with open('users.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    return redirect('login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = load_users()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in data and data[username]['password'] == password:
            print('성공적으로 로그인이 되었습니다.')
            return render_template('login.html')

        elif username in data and data[username]['password'] != password:
            print('사용자 비밀번호가 잘못되었습니다.')
            return render_template('login.html')

        elif username not in data and any(user['password'] == password for user in data.values()):
            print('사용자 이름이 잘못되었습니다.')
            return render_template('login.html')

        else:
            print('사용자 이름 및 비밀번호가 잘못되었습니다.')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)


###########################################
import json
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')     
def index():            #index 함수 선언  (호출을 해야 실행 가능)    
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
# 2. 프로젝트 폴더 안에 test.py 폴더 생성
