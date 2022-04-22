from flask import g
import sqlite3
import os

db_path = os.path.join(os.getcwd(), 'members.db')

def connect_db():
    # sql = sqlite3.connect('C:\\Users\\vishnu.adepu\\Desktop\\sqlite\\members.db')
    sql = sqlite3.connect(db_path)
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
