import json
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'yunyi'


def load_users():
    with open('users.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')     #listener
def index():
    return redirect('login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = load_users()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in data and data[username]['password'] == password:
            flash('Login was successful.')
            session['username'] = username  #세션에 저장
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

@app.route('/welcome')
def welcome():
    username = session.get('username')  #세션에서 꺼내기
    return render_template('welcome.html', username=username)

@app.route('/logout')
def logout():
    return redirect(url_for('login'))


if __name__ == '__main__':      #__name__ -> ?�스?�에???�정?�는 변??
    app.run(debug=True)
