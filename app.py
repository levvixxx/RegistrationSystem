from flask import Flask, render_template, request, redirect, session, url_for,send_file
from flask_sqlalchemy import SQLAlchemy
import random
from sqlalchemy import func
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'super-secret-key-2025'
db = SQLAlchemy(app)
url = "123"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), default="User") 


    

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for("glav"))

@app.route("/glav")
def glav():
    return render_template("index.html")  

@app.route('/login', methods=['GET', 'POST'])
def login():
    user_id = session.get("user_id")
    if user_id:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        name = request.form.get('username')
        passwordw = request.form.get('password')
        
        user = User.query.filter_by(username=name).first()

        if user:
            if user.password == passwordw:
                session["user_id"] = user.id
                return redirect(url_for("dashboard"))
        else:
            new_user = User(
                username=name, 
                password=passwordw, 
                role="User"
            )
            db.session.add(new_user)
            db.session.commit()
            session["user_id"] = new_user.id
            return redirect(url_for("dashboard"))
    return render_template('login.html')

 

@app.route('/dashboard')
def dashboard():
    user_id = session.get("user_id")
    user = db.session.get(User,user_id)
    if not user_id:
        return redirect(url_for("login"))
    return render_template('dashboard.html',user=user)

from flask import render_template

@app.route('/dashboard/<username>')
def showdashboard(username): 
    user = User.query.filter_by(username=username).first()
    if user:
        user_id = user.id
        return render_template('dashboardguest.html', user=user , user_id=user_id)
    else:
        return "Пользователь не найден", 404

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
