from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database import get_db_connection

auth_bp = Blueprint("auth", __name__)


# -------------------------------
# Login Page
# -------------------------------
@auth_bp.route("/", methods=["GET", "POST"])
def login():

    # If already logged in
    if session.get("logged_in"):
        return redirect(url_for("task.dashboard"))

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            session["logged_in"] = True
            session["username"] = user["username"]

            return redirect(url_for("task.dashboard"))

        else:
            flash("Invalid Username or Password", "danger")

    return render_template("login.html")


# -------------------------------
# Logout
# -------------------------------
@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))