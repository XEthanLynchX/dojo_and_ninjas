from flask_app import app

from flask import Flask, render_template, redirect, request, session

from flask_app.models import ninja_model, dojo_model

@app.route('/ninjas')
def ninja_form():
    return render_template('create_ninja.html', all_dojos = dojo_model.Dojo.get_all_dojos())

@app.route("/create/ninja", methods = ['POST'])
def save_ninja():
  ninja_model.Ninja.save_ninja(request.form)
  return redirect('/dojos')