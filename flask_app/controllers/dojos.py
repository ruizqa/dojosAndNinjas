from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/ninjas")
def form():
    dojos = Dojo.get_all()
    return render_template("add_ninja.html", dojos=dojos)

@app.route("/save_ninja", methods=["POST"])
def save_ninja():
    data = {
        "dojo": int(request.form["dojo"]),
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "age" : int(request.form["age"])
    }
    print(data)
    ninja = Ninja.save(data)
    return redirect('/dojos')
@app.route("/")
@app.route("/dojos")
def show_dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route("/save_dojo", methods=["POST"])
def save_dojo():
    data = {
        "name": request.form["name"],
        
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def show_dojo_ninjas(id):
    data={
        'id': id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("dojo_ninjas.html", dojo=dojo)

