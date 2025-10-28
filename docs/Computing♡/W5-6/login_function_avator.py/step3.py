# flask app 생성

# 1.프로젝트 폴더 안에 app.py 폴더 생성 후 폴터에 코드 넣음

import json
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

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
