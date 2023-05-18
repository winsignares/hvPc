from config.db import db, app, ma
from flask import Blueprint,render_template,request,jsonify
from model.admin import admin,adminSchema
routes_login= Blueprint("routes_login",__name__)

@routes_login.route("/indexlogin", methods= ["GET"])
def indexregistro():
    return render_template("/main/login.html")

@routes_login.route('/validarlogin', methods=['POST'])
def validar_inicio_sesion(email,password):
    email =admin.query.get(email)
    password =admin.get(password)
    db.session.commit()

    # Buscar el usuario en la base de datos
    usuario = admin.query.filter_by(email=email).first()

    # Verificar el inicio de sesión
    if usuario and usuario.password == password:
        return jsonify({'autenticado': True})
    else:
        return jsonify({'autenticado': False})
    
    