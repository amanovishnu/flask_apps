
# * this file is created based on the tutorials in module 3 of flask programming (Databases)

from webbrowser import get
from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ThisIsASecretKey'

def connect_db():
    sql = sqlite3.connect('C:\\Users\\vishnu.adepu\\Desktop\\sqlite\\data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    session.pop('name',None)
    return f"Hello, World"

@app.route('/home', methods=['GET','POST'], defaults={'name':'Mano Vishnu'})
@app.route('/home/<string:name>', methods=['GET','POST'])
def home(name):
    session['name'] = name
    db = get_db()
    cur = db.execute('select id, name, location from users;')
    results= cur.fetchall()
    return render_template('home.html', name=name, display=False, myList=[1,2,3,4], listOfDicts=[{'name':'Mano'},{'name':'Vishnu'}], results=results)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'NotInSession!'
    return jsonify({
        "name_session":name,
        "Name":"Mano Vishnu",
        "Profile":"Data Science Engineer"
        })

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'hi {name}, from {location} You\'re on the query page'

# * Eight, Tenth, Eleventh Lecture

@app.route('/theform',methods=['GET','POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        db = get_db()
        db.execute('insert into users (name, location) values(?, ?)',[name,location])
        db.commit()
        return redirect(url_for('home',name=name,location=location))

# * Ninth Lecture
@app.route('/processjson',methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']
    # Approach 1
    # return jsonify(result='success', name=name, location=location, randomlist=randomlist)
    # Approach 2
    return jsonify({  
        'result':'success',
        'name':name,
        'location':location,
        'randomlist':randomlist
    })

@app.route('/viewresults')
def viewresults():
    db = get_db()
    cur = db.execute('select id, name, location from users;')
    results = cur.fetchall()
    return f'The id is {results[2]["id"]}, The Name is {results[2]["name"]}, The Location is {results[2]["location"]}'


if __name__ == '__main__':
    app.run()