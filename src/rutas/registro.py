from config.db import db, app, ma
from flask import Blueprint,render_template, request
from model.admin import admin
routes_register= Blueprint("routes_register",__name__)

@routes_register.route("/indexregistro", methods= ["GET"])
def indexregistro():
    return render_template("/main/registro.html")

@routes_register.route('/guardaradmin',methods=['POST'])
def saveadmin():
    #request.form['title']
    fullname = request.form['full_name']
    print(fullname)
    new_admin = admin(fullname)
    db.session.add(new_admin)
    db.session.commit()
    return {'mensaje': 'informacion insrtada'}

