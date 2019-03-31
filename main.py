from flask import Flask, request, render_template, redirect
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_signup_form():
    return render_template("sign-up.html", title="Signup")


def validate_username_password(string):
    if len(string) == 0:
        return "Required"
    if not re.fullmatch('^.{3,20}$', string):
        return "Must be within character limit (3-20)."
    if re.search(r'\s', string):
        return "Spaces not allowed"
    return ''

def validate_password_verify(password, password_verify):
    if password != password_verify:
        return "Passwords do not match."
    return ''

def validate_email(email):
    if re.search(r'\s', email):
        return "Spaces not allowed"
    if not re.fullmatch('^.{3,20}$', email):
        return "Must be within character limit (3-20)."
    if len(email) > 0 and not re.fullmatch(r'^[^@.]+@[^@.]+\.[^@.]+$', email):
        return "Invalid email"
    return ''

@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    password_verify = request.form['password_verify']
    email = request.form['email']

    username_error = validate_username_password(username)
    password_error = validate_username_password(password)
    password_verify_error = validate_password_verify(password, password_verify)
    email_error = validate_email(email)

    if (len(username_error) == 0 and len(password_error) == 0
        and len(password_verify_error) == 0 and len(email_error) == 0):
        return redirect('/welcome?username={0}'.format(username))

    return render_template("sign-up.html", 
        title = "Signup", username = username, email = email,
        username_error = username_error, password_error = password_error,
        password_verify_error = password_verify_error, email_error = email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html", title="Welcome", username=username)

app.run()