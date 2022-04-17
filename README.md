# flask_apps
##### ways to create  a virtualenv
- anaconda: conda create --name <env name> python=<version>
- venv: py -m venv <env name>
- virtualenv: virtualenv <env name>

##### Ways to activate a virtual environment
- anaconda: conda activate <env name>
- venv:
    - <env name>/Scripts/activate (Windows)
    - <env name>/bin/activate (Linux)
- virtualenv:
    - <env name>/Scripts/activate (Windows)
    - <env name>/bin/activate (Linux)

##### Ways to deactivate a virtual environment
- anaconda: conda deactivate
- venv & virtualenv : deactivate

SET FLASK_APP = app.py

#### Ways to run a flask application
Method #1:
    `if __name__ == "__main__": app.run()`
    - Add the above piece of code to the bottom of app.py
    - python app.py (can directly run using python instead of flask run command & does not support app.run(debug=True) in new versions)
Method #2:
    - SET FLASK_APP = <filename.py> (by default app.py)
    - SET FLASK_DEBUG = 1 (To enable debugging in dev environment)
    - flask run

- The method for running a flask app in production is completely different.

#### different ways to send json data as response
    - jsonify(name="Mano", location="HYD", profile="DSE")
    - jsonify({"name":"Mano", "location":"HYD", "profile":"DSE"})
    - final output: 
        `{
            "name": "Mano",
            "location": "HYD",
            "profile": "DSE",
        }`
#### different ways to get request data 
- Query String  = request.args.get[<key>]
- form data = request.form[<key>]
- json data = request.get_json()['<key>'] 
- to know request method = request.method

#### multiple of enabling debugging in flask run
- SET FLASK_DEBUG=1 & flask run
- app.run(debug=True) & python app.py
- app.config['DEBUG'] = True & python app.py
- enabling debug mode provides a interactive shell kind of thing in browser in case of error for better debugging

#### how to save & retrieve data in sessions
 - prerequisites: define a secret session key using `app.config['SECRET_KEY] = 'SomeRandomKey'`
 - import session from flask `from flask import session`
 - save data = session['key']
 - fetch data = session['key]

##### ways to access content in html
- `{{ value }}` -> used for accessing a value for dynamic generation of html
- `{% text %} {% end text %}` -> used for implementing programing logic inside html using jinja
- `{% if <condition> %} {% else %} {% endif %}` & `{% for <condition> %} {% endfor %}`

#### template inheritance & include
- `{% block <blockname> %} {% endblock %}` -> to create a block in base template
- `{% extends 'base.html' %}` -> include base template in other files
- `{{ super() }}` -> use this special function to avoid overwriting of base template block contents
- `{{ url_for('static', filename='<absolute path of files form  static folder>') }}` -> to access files inside a html file
- `{% include '<filename.html>' %}` -> will include filename.html to a template, but default included file will have access to parent dynamic content & can be accessed by `{{ key }}`
