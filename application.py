import os
import json

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# this is the MODEL, the HTML is the viewer, and the Controller is application.py

db = SQL("sqlite:///emolog.db")


'''
@login_required: if the use tries to get into any of these routes, he will
be redirected to / to log in
'''
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # if method == POST aka user submits data
    if request.method == "POST":
        # then log user in

        ''' Confirm user types in username and password'''

        # If username is blank
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # IF password is blank
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # len(rows) is not 1 == username doesn't exist
        # check_password_hash: check if the typed in password
        # match the "hash" value in database


        ''' Database should store the hashes of the password, not the password itself'''
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        # store inside session the user's ID

        # User's ID is the ID value in the first row that shows up in our query
            # row[0]: first row representing the user
            # access a particular column: get value of the id column in the first row
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/invitation")

    # In else case, user just want to GET the login form
    # so we should display the login form to the user
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # access user's info
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

         # check if the user’s input is blank
        if not username:
            return apology("username is empty")

        # check if password input is blank:
        if not password:
            return apology("password is empty")

        # check if password matches confirmation
        if password != confirmation:
            return apology("passwords don't match")

        # check if username aready exist
        # query database for username:
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 0:
            return apology("username already exists")

        # if the 3 conditions are fulfilled, insert new data into users table
        # hash password before inserting
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))

        flash("Registered!")
        return redirect("/login")
    # if GET
    else:
        return render_template("registration.html")

@app.route("/invitation", methods=["GET", "POST"])
@login_required
def invitation():
    return render_template("invitation.html")


@app.route("/journal", methods=["GET", "POST"])
@login_required
def journal():
    if request.method == "POST":
        # access input data
        subject = request.form.get("subject")
        time = request.form.get("time")
        content = request.form.get("content")

        # insert new data into transactions table in finance.db
        db.execute("INSERT INTO entries (user_id, subject, entries, time) VALUES(?, ?, ?, ?)",
        session["user_id"], subject, content, time)

        flash("Entry posted!")
        return redirect("/invitation")

    # when user wants to GET the webpage, display form
    else:
        return render_template("journal.html")


@app.route("/history", methods=["GET", "POST"])
@login_required
def history():
    histories = db.execute("SELECT subject, time, entries FROM entries WHERE user_id = ? ORDER BY time DESC", session["user_id"])

    return render_template("history.html", histories=histories)


@app.route("/relationship", methods=["GET", "POST"])
@login_required
def relationship():
    if request.method == "POST":
        name = request.form.get("name")
        time = request.form.get("time")
        hours = request.form.get("hours")
        relationship = request.form.get("relationship")
        activity = request.form.get("activity")

        # hours is larger than 0
        try:
            value = float(hours)
            if value < 0:
                return apology("please enter a positive value")
        except ValueError:
            return apology("please enter a positive value")

        # insert new data
        db.execute("INSERT INTO tracker (user_id, name, time, hours, relationship, activity) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], name, time, hours, relationship, activity)

        flash("Submitted!")
        return redirect("/invitation")

    else:
        return render_template("relationship.html")


@app.route("/tracker", methods=["GET", "POST"])
@login_required
def tracker():

    # pies gives a list of dictionaries with keys: relationships, total hours
    pies = db.execute("SELECT relationship, SUM(hours) as total_hours FROM tracker WHERE user_id = ? GROUP BY relationship", session["user_id"])
    bar = db.execute("SELECT name, SUM(hours) as total_hours FROM tracker WHERE user_id = ? GROUP BY name ORDER BY total_hours DESC LIMIT 10", session["user_id"])
    tracks = db.execute("SELECT id, time, relationship, name, hours, activity FROM tracker WHERE user_id = ? ORDER BY time DESC", session["user_id"])
    return render_template("tracker.html", tracks=tracks, pies=pies, bar=bar)


