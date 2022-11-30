import os


from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Reload the template, switch it off if you don't need Auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")

@app.route("/register", methods=['GET'])
def register():
    return render_template("registration.html")