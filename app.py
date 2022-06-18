
from flask import Flask, jsonify,render_template,request
from data import *
app = Flask(__name__)

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        new_user = {
            "id" : len(users)+1,
            "fullname": request.json.fn,
            "username": request.json.un,
            "phonenumber": request.json.pn,
        }

        users.append(new_user)
        return jsonify(users)

    elif request.method == "GET":
        return render_template("html/signup.html")