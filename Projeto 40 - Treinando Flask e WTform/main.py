from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.config["SECRET_KEY"] = "teste"
bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[Length(min=8, max=20)])
    submit = SubmitField("Log In")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new_login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    print(login_form.email.data, login_form.password.data)
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    else:
        return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
