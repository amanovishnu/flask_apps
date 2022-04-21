from flask import g
import sqlite3
import psycopg2
from psycopg2.extras import DictCursor

# def connect_db():
#     sql = sqlite3.connect('C:\\Users\\vishnu.adepu\\Desktop\\sqlite\\questions.db')
#     sql.row_factory = sqlite3.Row
#     return sql

# def get_db():
#     if not hasattr(g, 'sqlite3'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db

def connect_db():
    url = 'postgres://nwzlfedgiqqquv:5c85f2f0c041b45afb59c07b5f7662777c65b8d8c03de049828626b689771905@ec2-34-192-210-139.compute-1.amazonaws.com:5432/dfc8tntu70ra3c'
    conn = psycopg2.connect(url,cursor_factory=DictCursor)
    conn.autocommit = True
    sql = conn.cursor()
    return conn,sql

def get_db():
    db = connect_db()
    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]
    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]
    
    return g.postgres_db_cur

def init_db():
    db = connect_db()
    db[1].execute(open('questions.sql','r').read())
    db[1].close()
    db[0].close()

def init_admin():
    db = connect_db()
    db[1].execute('update users set admin = True where name = %s', ('admin', ))
    db[1].close()
    db[0].close()