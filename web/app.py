from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)
users = {}

@app.route("/")
def hello():
    return render_template("join.html")

@app.route("/login" ,methods=['POST'])
def login():
    id = request.form['id']
    pw = request.form['pw']
    if id in users:
        if users[id] == hashlib.sha1(pw).hexdigest():
            return "login ok"
        else:
            return "login fail"
    else:
        return"login fail" 

@app.route("/name")
def name():
    return "rnjsgml"

@app.route("/join", methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        if id in users:
            users[id] = hashlib.sha1(pw).hexdigest()
        else:
            return "duplicate!!!"
        return "join ok"
    return render_template("join.html")


@app.route("/add")
@app.route("/add/<int:num1>")
@app.route("/add/<int:num1>/<int:num2>")
def add(num1=None, num2=None):
    if num1 is None or num2 is None:
        return "/add/num1/num2"
    return str(num1 + num2)

