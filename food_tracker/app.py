from cmath import log
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

    date_results = list()
    for i in results:
        single_date = {}
        single_date['date'] = i['entry_date']
        d = datetime.strptime(str(i['entry_date']), '%Y%m%d')
        single_date['entry_date'] = datetime.strftime(d,'%B %d, %Y')
        date_results.append(single_date)
    
    return render_template('home.html',results=date_results)

@app.route('/view/<date>', methods=['GET','POST']) # date will be in the format 20220501
def view(date):
    
    db = get_db()
    cur = db.execute('select id, entry_date from log_date where entry_date = ?',[date])
    date_result = cur.fetchone()
    d = datetime.strptime(str(date_result['entry_date']),'%Y%m%d')
    pretty_date = datetime.strftime(d,"%B %d, %Y")

    if request.method == 'POST':
        db.execute('insert into food_date (food_id, log_date_id) values (?, ?)',[request.form['food-select'], date_result['id']])
        db.commit()

    # logic to fetch all food items added so far
    food_cur = db.execute('select id, name from food;')
    food_results = food_cur.fetchall()

    # logic to fetch differnet food items eaten in a given day
    log_cur = db.execute('''select food.name, food.protein, food.carbohydrates, food.fat, food.calories from food
                            join food_date on food.id = food_date.food_id
                            join log_date on food_date.log_date_id = log_date.id 
                            where log_date.entry_date = ?''',[date])
    log_results = log_cur.fetchall()

    # logic to fetch sum of total food eaten in a given day
    total_cur = db.execute('''select sum(food.protein) as protein, sum(food.carbohydrates) as carbohydrates, sum(food.fat) as fat, sum(food.calories) as calories from food
                            join food_date on food.id = food_date.food_id
                            join log_date on food_date.log_date_id = log_date.id 
                            where log_date.entry_date = ?''',[date])
    total_results = total_cur.fetchone()

    return render_template('day.html', entry_date = date_result['entry_date'], pretty_date= pretty_date, food_results=food_results, log_results=log_results, total_results=total_results)

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