import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session
from flask_session.__init__ import Session
from werkzeug.security import check_password_hash, generate_password_hash


fdrct = os.path.dirname(os.path.abspath(__file__))
# Configure application
app = Flask(__name__)

# Reload the template, switch it off if you don't need Auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True



app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET","POST"])
def login():

    session.clear()

    if request.method == "POST":
        
        username=request.form.get("username")
        password=request.form.get("password")

        if not username or username == None:
            return redirect("errorpage.html")
        elif not password or password == None:
            return redirect("errorpage.html")
        else:
            db=sqlite3.connect(fdrct + "///finarm.db")
            cur = db.cursor()
            query = "SELECT password FROM users WHERE username = '{usrnm}'".format(usrnm=username)
            res = cur.execute(query)   
            res = res.fetchall()[0][0]
            if check_password_hash(res, password):
                session["username"] = username
                return render_template("homepage.html")
            else:
                return render_template("login.html")
    
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():
    
    if request.method == "POST":
        firstname=request.form.get("firstname")
        lastname=request.form.get("lastname")
        password=request.form.get("password")
        username=request.form.get("username")
        confirmpassword=request.form.get("confirmpassword")
        email=request.form.get("email")
        phone=request.form.get("phone")

        if not firstname or  firstname == None:
            return redirect("errorpage.html")
        elif not lastname or lastname == None:
            return redirect("errorpage.html") 
        elif not email or email == None:
            return redirect("errorpage.html")
        elif not password or password == None or password != confirmpassword:
            return redirect("errorpage.html")
        elif not phone or phone == None:
            return redirect("errorpage.html")
        else:
            hashval = generate_password_hash(
                    password, method='pbkdf2:sha256', salt_length=9)
        db=sqlite3.connect(fdrct + "///finarm.db")
        cur = db.cursor()
        query = "SELECT username FROM users WHERE username = '{usrnm}'".format(usrnm=username)
        res = cur.execute(query)   
        res = res.fetchall()
        print
        if len(res) == 0:
            query1 = "INSERT INTO users(firstname,lastname,username,password,email,phone) VALUES('{fn}','{ln}','{usr}','{pwd}','{eml}','{phn}')".format(fn=firstname,ln=lastname,usr=username,pwd=hashval,eml=email,phn=phone)
            cur.execute(query1)
            db.commit()
        else:
            return render_template("errorpage.html")
    else:
        return render_template("registration.html")

    return render_template("registration.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")
        

@app.route("/logout")
def logout():
 # Forget any user_id
    session.clear()
# Redirect user to login form
    return render_template("index.html")



