from common.token import *
from config.db import db,ma,app
from flask import Flask, Blueprint, redirect, request, jsonify, json, session
from model.admin import admin,adminSchema

routes_admin= Blueprint("routes_admin",__name__ )

#ADMINS
admin_Schema= adminSchema()
admins_Schema= adminSchema(many=True)

@app.route('/admins', methods=['GET'])
def mostrar_admin():
    returnall = admin.query.all()
    
    result_admins = admins_Schema.dump(returnall)
    return jsonify(result_admins)


#crud de admins
@app.route('/eliminar_admins/<id>', methods=['GET'])
def eliminar_admin(id):
    admins= admin.query.get(id)
    db.session.delete(admins)
    db.session.commit()
    return jsonify(adminSchema.dump(admins))

@app.route('/actualizar_clients', methods=['POST'])
def actualizar_admin():
    id= request.json['id']
    datos= request.json['full_name','telefono','direccion','email','password','id_genero']
    admins= admin.query.get(id)
    admins.datos= datos
    db.session.commit()
    return redirect('/admins') 

@app.route('/guardar_admins',methods= ['POST'])
def guardar_admin():
    addadmin= request.json['full_name','telefono','direccion','email','password','id_genero']
    print(addadmin)
    new_admin= admin(addadmin)
    db.session.add(new_admin)
    db.session.commit()
    return redirect('/admins')


