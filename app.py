import math
import os
import sqlite3
import json

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

@app.route("/home")
def home():
    return render_template("homepage.html")

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

@app.route("/addfininfo", methods=["GET","POST"])
def addfininfo():
    if request.method=="POST":
        cardname = request.form.get("cardname")
        amountused = request.form.get("amountused")
        limit = request.form.get("limit")
        cashapr = request.form.get("cashapr")
        baltranapr = request.form.get("baltranapr")
        purchaseapr = request.form.get("purchaseapr")
        benefits = request.form.get("benefits")
        username = session["username"]

        if not cardname or cardname == None:
            return render_template("errorpage.html")
        elif not amountused or amountused == None:
            return render_template("errorpage.html")
        elif not limit or limit == None:
            return render_template("errorpage.html")
        elif not cashapr or cashapr == None:
            return render_template("errorpage.html")
        elif not baltranapr or baltranapr == None:
            return render_template("errorpage.html")
        elif not purchaseapr or purchaseapr == None:
            return render_template("errorpage.html")
        elif not benefits or benefits == None:
            return render_template("errorpage.html")
        else:
            db=sqlite3.connect(fdrct + "///finarm.db")
            cur = db.cursor()
            query1 = "INSERT INTO fininfo(ccname,ccused,cclimit,cashapr,balapr,purapr,username,benefits) VALUES('{ccn}','{ccu}','{ccl}','{capr}','{blapr}','{purapr}','{usrnm}','{bnfts}')".format(ccn=cardname,ccu=amountused,ccl=limit,capr=cashapr,blapr=baltranapr,purapr=purchaseapr,usrnm=username,bnfts=benefits)
            cur.execute(query1)
            db.commit()
    else:    
        return render_template("finadd.html")

    return render_template("finadd.html")        

@app.route("/analysis")
def analysis():
        totusdamt=0
        totavlamt=0
        db=sqlite3.connect(fdrct + "///finarm.db")
        cur = db.cursor()
        query = "SELECT * FROM fininfo WHERE username = '{usrnm}'".format(usrnm=session["username"])
        res = cur.execute(query)   
        finresults = res.fetchall()
        simulationdata={}
        simlist=[]
        


        for fin in finresults:
            simulationdata['cardname'] = fin[1]
            simulationdata['balance'] = fin[2]
            simulationdata['minbal'] = 200
            aprpur = float(fin[6])
            daily_rate = aprpur/100/365 
            r1 = -1/30
            r2 = math.log(1+ (int(fin[2])/200) * (1- math.pow((1 + (daily_rate)), 30)))
            r3 = math.log(1+daily_rate)
            simulationdata['paymenttime'] = math.ceil(r1 * (r2/r3))
            totusdamt += int(fin[2])
            totavlamt += int(fin[3])
            debtrtn = totusdamt/totavlamt
            fininfores = json.dumps(simulationdata)
            simlist.append(json.loads(fininfores))
            print(simlist)
        return render_template("analysis.html",vals=finresults,val2=debtrtn,simdata=simlist)

@app.route("/logout")
def logout():
 # Forget any user_id
    session.clear()
# Redirect user to login form
    return render_template("index.html")



