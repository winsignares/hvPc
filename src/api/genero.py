from config.db import db,ma,app
from flask import Flask, Blueprint, redirect, request, jsonify, json, session
from model.genero import generos,generosSchema

routes_genero= Blueprint("routes_genero",__name__ )

#generos
genero_Schema= generosSchema()
generos_Schema= generosSchema(many=True)

@app.route('/generos', methods=['GET'])
def mostrar_generos():
    returnall = generos.query.all()
    
    result_generos = generos_Schema.dump(returnall)
    return jsonify(result_generos)


#crud de generos
@app.route('/eliminar_generos/<id>', methods=['GET'])
def eliminar_generos(id):
    genero= generos.query.get(id)
    db.session.delete(genero)
    db.session.commit()
    return jsonify(generosSchema.dump(genero))

@app.route('/actualizar_generos', methods=['POST'])
def actualizar_generos():
    id= request.json['id']
    datos= request.json['genero']
    genero= generos.query.get(id)
    genero.datos= datos
    db.session.commit()
    return redirect('/generos') 

@app.route('/guardar_generos',methods= ['POST'])
def guardar_genero():
    addgenero= request.json['genero']
    print(addgenero)
    new_genero= generos(addgenero)    
    db.session.add(new_genero)
    db.session.commit()
    return redirect('/generos')
