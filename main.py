from flask import Flask, request, render_template
import os
from jinja2 import Environment, PackageLoader
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():

    return render_template('signup_template.html')
    


@app.route("/login", methods=['POST'])
def authentication():
    username = request.form["username"]
    password = request.form["password"]
    verifiedpass = request.form["verify_password"]
    email = request.form["email"]
    verified_email = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email)
    
    output = []
    infoList = [("usernameerror", username), ("passworderror", password), ("verifiederror", verifiedpass)]
    for key, value in infoList:
        if value == "":
            output.append(key)  
    if len(output) > 0:
        return render_template("signup_template.html", username=username, email=email, generalerror="Please fill out all required fields")
    if len(username) < 3 or len(username) > 20:
        return render_template('signup_template.html', username=username, email=email, usernameerror="Must be 3-20 characters and no spaces")
    for char in username:
        if char.isspace():
            return render_template('signup_template.html', username=username, email=email, usernameerror="Must be 3-20 characters and no spaces")
    if len(password) < 3 or len(password) > 20:
        return render_template('signup_template.html', username=username, email=email, passworderror="Must be 3-20 characters and no spaces")
    for char in password:
        if char.isspace():
            return render_template('signup_template.html', username=username, email=email, passworderror="Must be 3-20 characters and no spaces")
    if verifiedpass != password:
        return render_template('signup_template.html', username=username, email=email, verifiederror="Passwords do not match")
    if email != '':
        if not verified_email:
            return render_template('signup_template.html', username=username, email=email, emailerror="Invalid email format")
    return render_template("welcome.html", username=username)
if __name__ == '__main__':
    app.run()