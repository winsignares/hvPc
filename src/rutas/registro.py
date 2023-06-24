from config.db import db, app, ma
from flask import Blueprint,render_template, request
from model.admin import admin
routes_register= Blueprint("routes_register",__name__)

@routes_register.route("/indexregistro", methods= ["GET"])
def indexregistro():
    return render_template("/main/registro.html")

@routes_register.route('/guardar_admin', methods= ["POST"])
def saveadmin():
    full_name = request.form['fullname']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    email = request.form['email']
    password = request.form['password']  
    id_genero = request.form['id_genero']
    print(full_name)
    new_admin = admin(full_name,telefono,direccion,email,password,id_genero)
    
    db.session.add(new_admin)
    db.session.commit()
    return "ok"

