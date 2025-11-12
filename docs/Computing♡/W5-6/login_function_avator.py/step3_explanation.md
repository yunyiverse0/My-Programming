### import json
- json 파일을 다루는 내장 모듈 (users.json 읽기용)

### from flask import Flask, render_template, request, redirect, url_for, session, flash
- flask 안의 특정 기능만 선택적으로 불러옴
- flask.request처럼 앞에 flask.을 붙일 필요 없음
- flask: 모듈 이름  
- Flask: 클래스 이름 (서버 생성용)

---

### app = Flask(__name__)
- Flask 애플리케이션(웹 서버) 생성
- __name__은 현재 파일 이름을 의미, Flask가 경로를 찾을 때 사용

### app.secret_key = 'yunyi'
- flash와 session을 안전하게 사용하기 위한 서명 키

---

### def load_users():
```python
with open('users.json', 'r', encoding='utf-8') as f:
    return json.load(f)
