from operator import ge
from flask import Flask, render_template, g, request, jsonify
import sqlite3
from datetime import datetime


app = Flask(__name__)

def connect_db():
    sql = sqlite3.connect('C:\\Users\\vishnu.adepu\\Desktop\\sqlite\\food_log.db')
    sql.row_factory = sqlite3.Row # converts tuples to dictionary
    return sql

def get_db():
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/', methods=['GET','POST'])
def index():
    db = get_db()
    
    if request.method == 'POST':
        dt = datetime.strptime(request.form['date'],'%Y-%m-%d')
        db_dt = datetime.strftime(dt,'%Y%m%d')
        db.execute('insert into log_date (entry_date) values (?)',[db_dt])
        db.commit()
    
    cur = db.execute('select entry_date from log_date order by entry_date desc;')
    results = cur.fetchall()

    pretty_results = list()
    for i in results:
        single_date = {}
        d = datetime.strptime(str(i['entry_date']), '%Y%m%d')
        single_date['entry_date'] = datetime.strftime(d,'%B %d, %Y')
        pretty_results.append(single_date)
    
    return render_template('home.html',results=pretty_results)

@app.route('/view')
def view():
    return render_template('day.html')

@app.route('/food', methods=['GET','POST'])
def food():
    db = get_db()
    if request.method == 'POST':
        name = request.form['food-name']
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])
        calories = protein * 4 + carbohydrates * 4 + fat * 9
        db.execute('insert into food (name, protein, carbohydrates, fat, calories) values (?, ?, ?, ?, ?)',[name, protein, carbohydrates, fat, calories])
        db.commit()
    
    curr = db.execute('select * from food order by id desc;')
    results = curr.fetchall()
    return render_template('add_food.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)