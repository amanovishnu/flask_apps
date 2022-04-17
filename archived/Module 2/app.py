
# * this file is created based on the tutorials in module 2 of flask programming (Basics of Templates)

from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ThisIsASecretKey'

@app.route('/')
def index():
    session.pop('name',None)
    return f"Hello, World"

@app.route('/home', methods=['GET','POST'], defaults={'name':'Mano Vishnu'})
@app.route('/home/<string:name>', methods=['GET','POST'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False, myList=[1,2,3,4], listOfDicts=[{'name':'Mano'},{'name':'Vishnu'}])

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

# Approach 1
# @app.route('/theform', methods=['POST','GET'])
# def theform():
#     if request.method == 'GET':
#         return '''
#             <form method="POST" action="process">
#                 <input type="text" name="name"/>
#                 <input type="text" name="location"/>
#                 <input type="submit" value="Submit"/>
#             </form>
#         '''
#     else:
#         name = request.form['name']
#         location = request.form['location']
#         return f'<h1>Hello {name}, from {location}, you\'re details are saved successfully</h1>'

# Approach 2
# @app.route('/theform', methods=['GET'])
# def theform():
#     return '''
#         <form method="POST" action="/theform">
#             <input type="text" name="name"/>
#             <input type="text" name="location"/>
#             <input type="submit" value="Submit"/>
#         </form>
#     '''

# @app.route('/theform',methods=['POST'])
# def process():
#     name = request.form['name']
#     location = request.form['location']
#     return f'<h1>Hello {name}, from {location}, you\'re details are saved successfully</h1>'

# @app.route('/process', methods=['POST'])
# def process():
#     name = request.form['name']
#     location = request.form['location']
#     return f'<h1>Hello {name}, from {location}, you\'re details are saved successfully</h1>'

@app.route('/theform',methods=['GET','POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
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



if __name__ == '__main__':
    app.run()