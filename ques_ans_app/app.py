from flask import Flask, render_template, g, request, url_for, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
from database import get_db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.urandom(24)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    user = None
    if 'user' in session:
        user = session['user']
    return render_template('home.html', user=user)

@app.route('/register', methods=['GET','POST'])
def register():
    db = get_db()
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form['password'], method='sha256')
        db.execute('insert into users (name, password, expert, admin) values(?, ?, ?, ?)',[request.form['name'], hashed_password, '0', '0'])
        db.commit()
        return 'user created successfully'

    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    db = get_db()
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user_cur = db.execute('select id,name, password from users where name=?',[name])
        user_result = user_cur.fetchone()
        if check_password_hash(user_result['password'], password):
            session['user'] =  user_result['name']
            return 'The password is correct'
        else:
            return 'Wrong Password'
    return render_template('login.html')

@app.route('/question')
def question():
    return render_template('question.html')

@app.route('/answer')
def answer():
    return render_template('answer.html')

@app.route('/ask')
def ask():
    return render_template('ask.html')

@app.route('/unanswered')
def unanswered():
    return render_template('unanswered.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)