from common.token import *
from config.db import db,ma,app
from flask import Flask, Blueprint, redirect, request, jsonify, json, session
from model.pc import pc,pcsSchema

routes_pcs= Blueprint('routes_pcs', __name__)

#pcs 
pc_Schema= pcsSchema()
pcs_Schema= pcsSchema(many= True)

#crud pcs
@app.route('/pcs', methods=['GET'])
def pcs():
    returnall= pc.query.all()
    result_pc= pcs_Schema.dump(returnall)
    return jsonify(result_pc)

@app.route('/eliminar_pcs/<id>', methods=['GET'])
def eliminar_pcs(id):
    pcs= pc.query.get(id)
    db.session.detete(pcs)
    db.session.commit()
    return jsonify(pcsSchema.dump(pcs))

@app.route('/actualizar_pcs', methods=['POST'])
def actualizar_pcs():
    id= request.json['id']
    datos= request.json['marca','serie','capacidad_Ram','tarjeta_grafica','capacidad_discoDuro','procesador','sistema_operativo','fecha_adquisicion']
    pcs= pc.query.get(id)
    pcs.datos= datos
    db.session.commit()
    return redirect('/pcs')

@app.route('/guardar_pcs', methods=['POST'])
def guardar_pcs():
    addpcs= request.json['marca','serie','capacidad_Ram','tarjeta_grafica','capacidad_discoDuro','procesador','sistema_operativo','fecha_adquisicion']
    print(addpcs)
    newpc= pc(addpcs)
    db.session.add(newpc)
    db.session.commit()
    return redirect('/pcs')


















