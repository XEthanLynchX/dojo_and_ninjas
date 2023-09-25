from flask_app import app

from flask import Flask, render_template, redirect, request

from flask_app.models import dojo_model

#add crud routing 
# create route - render a form to create and hava a Post method route 
# read-view all, view one

@app.route("/dojos")
def index():
    return render_template('view_all_dojos.html', all_dojos= dojo_model.Dojo.get_all_dojos())

@app.route("/create/dojo", methods = ['POST'])
def save_dojo():
    dojo_model.Dojo.save_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('view_one_dojo.html', dojo= dojo_model.Dojo.get_one_with_ninjas(data))


