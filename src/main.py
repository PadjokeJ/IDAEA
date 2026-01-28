from flask import Flask, render_template, request, redirect
import flask_login

from dotenv import load_dotenv
from os import getenv
import json

import password
import database

load_dotenv("local.env")

app = Flask(__name__)
app.secret_key = getenv("SECRET")

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
  pass

@login_manager.user_loader
def user_loader(email):
  users = database.get_users()
  
  if email not in users:
    return
  
  user = User()
  user.id = email
  return user

@login_manager.request_loader
def request_loader(request):
  email = request.form.get("email")
  return user_loader(email)

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    if flask_login.current_user.is_authenticated:
      return redirect("/home")
    return render_template("login.html")
  
  email = request.form["email"]
  if email in get_users() and get_login(email, bytes(request.form["password"], "utf-8")):
    user = User()
    user.id = email
    flask_login.login_user(user)
    return redirect("/home")

@app.route("/logout")
def logout():
  flask_login.logout_user()
  return redirect("/login")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)

