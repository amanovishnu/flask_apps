from ast import Pass
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "ItsMySecretKey"

class LoginForm(FlaskForm):
    username = StringField(label="username", name="username", default="amanovishnu")
    password = PasswordField(label="password", name="password", default="random")


@app.route('/',methods=['GET','POST'])
def index():
    form = LoginForm()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
