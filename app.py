import os

from flask import Flask, redirect, render_template, jsonify, request, session
from flask_session import Session
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/")
def index():
    # go to homepage
    print("_______-------")
    return render_template("index.html")

@app.route("/homepage", methods=["GET"])
def homepage():
    return render_template("homepage.html")
