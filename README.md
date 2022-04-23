# flask_apps

## Ways to create  a virtualenv

- anaconda: `conda create --name <env name> python=<version>`
- venv: `py -m venv <env name>`
- virtualenv: `virtualenv <env name>`

## Ways to activate a virtual environment

- anaconda: `conda activate <env name>`
- virtaulenv/venv:
  - `<env name>/Scripts/activate (Windows)`
  - `<env name>/bin/activate (Linux)`

## Ways to deactivate a virtual environment

- anaconda: `conda deactivate`
- venv/virtualenv : `deactivate`

## Ways to run a flask application

**Method 1:**

- `if __name__ == "__main__": app.run(debug=True)`
- Add the above piece of code to the bottom of app.py
- `python app.py` : can directly run flask app using python instead of flask run

**Method 2:**

- `SET FLASK_APP = <filename.py>` (by default app.py)
- `SET FLASK_DEBUG = 1` (To enable debugging in dev environment)
- `flask run`
- The method for running a flask app in production is completely different.

## Different ways to send json data as response

- `jsonify(name="Mano", location="HYD", profile="DSE")`
- `jsonify({"name":"Mano", "location":"HYD", "profile":"DSE"})`

```json
        {
            "name": "Mano",
            "location": "HYD",
            "profile": "DSE",
        }
```

## Different ways to get request data

- Query String = `request.args.get[<key>]`
- form data = `request.form[<key>]`
- json data = `request.get_json()['<key>']`
- to know request method = `request.method`

## Multiple ways of enabling debugging in flask run

- `SET FLASK_DEBUG=1 & flask run`
- `app.run(debug=True) & python app.py`
- `app.config['DEBUG'] = True & python app.py`
- enabling debug mode provides a interactive shell kind of thing in browser in case of error for better debugging

## How to save & retrieve data in sessions

- prerequisites: define a secret session key using `app.config['SECRET_KEY] = 'SomeRandomKey'`
- import session from flask `from flask import session`
- save data = `session['key']`
- fetch data = `session['key]`
- remove key from session = `session.pop(<key>, None)`

## Ways to access content in html

- `{{ value }}` -> used for accessing a value for dynamic generation of html
- `{% text %} {% end text %}` -> used for implementing programing logic inside html using jinja
- `{% if <condition> %} {% else %} {% endif %}` & `{% for <condition> %} {% endfor %}`

## Template inheritance & include

- `{% block <blockname> %} {% endblock %}` -> to create a block in base template
- `{% extends 'base.html' %}` -> include base template in other files
- `{{ super() }}` -> use this special function to avoid overwriting of base template block contents
- `{{ url_for('static', filename='<absolute path of files form  static folder>') }}` -> to access files inside a html file
- `{% include '<filename.html>' %}` -> will include filename.html to a template, but default included file will have access to parent dynamic content & can be accessed by `{{ key }}`
- `g` is a global object in flask, which allows us to store data which is accessible to all parts of application when app is running.
- `@app.teardown_appcontext` is automatically called whenever a route returns, will be used to close db connection.
- `hasattr()` method can be used to check if a key exists in a dict or not
- `sql.connect(<path to db>)` -> to connect to sqlite db
- `sql.row_factory = sqlite3.Row`  -> to convert response from a tuple to a dict
- `db = get_db() -> cur = db.execute(<sql statement>) -> cur.fetchall()` -> steps to read data form sql
- `db = get_db() -> db.execute(<sql statement>) -> db.commit()` -> steps to write data to sql
- `db.execute('insert into users (name, location) values (?, ?)', ['Geek','USA'])` -> to prevent sql injection.
- `cur.fetchall()` fetches all records whereas `fetchone()` fetches only one record.
- `cur.fetchall()` -> returns a list of dictionaries
- `cur.fetchone()` -> returns a single dictionary

## Deploy app on amazon lightsail

- its a service for virtual servers, upload code to server and access it using ip address of server.
- other alternatives are python anywhere and heroku (easier & beginner friendly)
- `os -> ubuntu -> sudo apt-get update -> sudo apt-get install nginx`
- start nginx: `sudo /etc/init.d/nginx start`
- remove default configuration: `sudo rm /etc/nginx/sites-enabled/default`
- create a new file with flask settings: `sudo touch /etc/nginx/sites-available/flask_settings`
- create a link between files: `sudo ln -s /etc/nginx/sites-available/flask_settings /etc/nginx/sites-enabled/flask_settings`
- open the file: `sudo vi /etc/nginx/sites-enabled/flask_settings`

```bash
server {
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

- proxy_pass handles/redirects the incoming https requests to application server
- nginx is a proxy server, it handles http requests
- gunicorn is a application server, similar to flask development server.
- restart the nginx service : `sudo /etc/init.d/nginx restart`
- `which python` : to check which  version of python (2/3) is installed.
- `sudo apt-get install python3-pip` : to instal pip
- `sudo pip3 install virtualenv` : to install virtualenv
- `virtualenv <env name>` :to create a new env
- `source <env name>/bin/activate` : to activate the environment
- `python -V | python --version` : to check the version of python
- `pip3 install flask gunicorn` : to install flask and gunicorn application server
- no need of `app.run()`, gunicorn will take care of this
- `gunicorn app:app` : to start the server (`gunicorn <filename>:<app name>`)
- `which git` : to check if git is installed or not, if installed where it's installed

## Deployment steps in heroku

- heroku does not have native support for sqlite3
- create a `Procfile` : it instructs heroku web workers on how to run the app
- Procfile -> `web: gunicorn app:app` -> tells heroku web worker to run `gunicorn app:app`
- `heroku create` : creates a new app in heroku
- `git push heroku master` : commit changes and push to heroku master -> app will be deployed to heroku
- `heroku logs tail` : returns the last few lines of logs

## Security in flask

- `werkzeug.security` module provides security related methods in flask
- `generate_password_hash` is used to generate a password hash.
- `check_password_hash` is used to check the password hash.
- we can import these two methods from `from werkzeug.security import generate_password_hash, check_password_hash`
- `password = generate_password_hash(<original password>, method=<hashing technique like sha256>)`
- `check_password_hash(<hashed_pwd>,<actual_pwd>)` : returns true if both passwords match else returns false

## Generating session key in flask application

```python
import os
app.config['SECRET_KEY'] = os.urandom(24)
```

## SQL tips

- always use `is` instead of `=` when querying for NULL values;
- sql update query : `update users set name = <name > where id = <id>;`
- sql delete query : `delete from users where id = <id>;`

## Macro's in flask

- marcos are pretty much like functions in python. where it can be called from template and it can returns different output based on input
- `{% macro <function_name(params)> %} <html content> {% endmacro %}` : to create a macro function.
- `{% from <filename.html> import <function_name >%}` : to import macro to a template
- `{{ <function_name(params)> }}` : to call a macro inside a template.

```html
<!-- to define a macro -->
{% macro show_links(user) %}
    <!-- html logic -->
{% endmacro %}

<!-- to use a macro -->
{% from "show_links.html" import show_links %}
{{ show_links(user )}}
```

## Authentication of api's in flask

- for basic authentication use `request.authorization.username` & `request.authorization.password` from request module.
- pass status code with return statement `return jsonify(), <status code>`
- example: `return jsonify({"message":"failed"}), 403`

## Creating a decorator in flask

- always place the custom decorator below the flask decorators

```python
from functools import wraps
def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username = api_username and auth.password == api_password:
            return f(*args, **kwargs)
        else:
            return jsonify({"message":"authorization failed"}), 403
    return decorated
```

## General tips in flask

- `os.getcwd()` -> returns the path of current working directory
- `os.path.join(<path_one>,<path_two>)` -> appends path_two to path_one.
- `pip freeze > requirements.txt` -> generates a requirements.txt file
- `app.config.form_pyfile(<filename.cfg>)` -> to load config details from an external config file

## Flask SQLAlchemy

- Steps to define a table using SQLAlchemy

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app) # creates a db object

class Test(db.Model): # defines a db table
    id = db.Column(db.Integer, primary_key=True) # defines table columns
```

- Steps to create a table defined using SQLAlchemy

```python
from application import db
db.create_all()
```

```python
# add data using SQLAlchemy
anthony = Member(name= 'anthony', password= 'secret', email= 'email@gmail.com', joined_date= datetime.today())
db.session.add(anthony)
db.session.commit()

# delete data using SQLAlchemy
db.session.delete(anthony)
db.session.commit()

# update data using SQLAlchemy
anthony.password = 'newSecretPassword'
anthony.email = 'anthony@gmail.com'
db.session.commit()

# read data using SQLAlchemy
all_record = Member.query.all() # gets all data in member table.
first_record = Member.query.first() # gets the first row from member table
record_filter_by = Member.query.filter_by(name= 'steven') # fetches all matching records
first_record_filter_by = Member.query.filter_by(name= 'steven').first() # fetches first matching records
only_filter = Member.query.filter(Member.name.endswith('ert')).all() # fetches all records having name ends with 'ert'
q = Member.query.filter(Member.name == 'mano').all() # equal to
q = Member.query.filter(Member.name != 'mano').all() # not equal to
q = Member.query.filter(Member.name.like('%no')).all() # like
q = Member.query.filter(Member.name.not_like('%no')).all() # not like
q = Member.query.filter(Member.name.in_(<list of entries>)).all() # in
q = Member.query.filter(~Member.name.in_(<list of entries>)).all() # not in
q = Member.query.filter(Member.email == None).all() # null value
q = Member.query.filter(Member.email != None).all() # not null
q = Member.query.filter(Member.name == 'mano').filter(Member.email == 'geeky@gmail.com').all() # and -> 1.Generative way
q = Member.query.filter(Member.name == 'mano', Member.email == 'geeky@gmail.com').all() # and -> 2
q = Member.query.filter(db.and_(Member.name == 'mano', Member.email == 'geeky@gmail.com')).all() # and -> 3
q = Member.query.filter(db.or_(Member.name == 'mano', Member.email == None)).all() # or
q = Member.query.order_by(Member.name).all() # order by asc
q = Member.query.order_by(Member.name.desc()).all() # order by desc
q = Member.query.limit(<int>).all() # limit
q = Member.query.offset(<int>).all() # offset
q = Member.query.count() # count
q = Member.query.filter(Member.id <in equality operator> 1).all() # in equality

```

## Working with flask-wtf

- install flask-wtf using `pip install flask-wtf`

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
```
