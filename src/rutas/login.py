from config.db import db, app, ma
from flask import Blueprint,render_template,request,jsonify,session
from model.admin import admin,adminSchema
from common.token import *
routes_login= Blueprint("routes_login",__name__)

@routes_login.route("/indexlogin", methods= ["GET"])
def indexregistro():
    return render_template("/main/login.html")

@routes_login.route('/validarlogin', methods=['POST'])
def validar_inicio_sesion():
    email =request.json['email']
    password =request.json['password']
    

    # Buscar el usuario en la base de datos
    usuario = admin.query.filter_by(email=email,password=password).first()

    # Verificar el inicio de sesión
    if usuario:
        usuario.generate_token()
        db.session.commit()
        print("paso")
        href="/fronted/indexhome"
        return href
   
    

