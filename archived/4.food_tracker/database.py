from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('C:\\Users\\vishnu.adepu\\Desktop\\sqlite\\food_log.db')
    sql.row_factory = sqlite3.Row # converts tuples to dictionary
    return sql

def get_db():
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db