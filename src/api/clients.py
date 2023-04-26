from common.token import *
from config.db import db,ma,app
from flask import Flask, Blueprint, redirect, request, jsonify, json, session
from model.clients import clients,clientesSchema

routes_clients= Blueprint("routes_client",__name__)

#clients
client_Schema= clientesSchema()
clients_Schema= clientesSchema(many=True)

@app.route('/clients', methods=['GET'])
def client():
    returnall = clients.query.all()
    
    result_clients = clients_Schema.dump(returnall)
    return jsonify(result_clients)


#crud de clients
@app.route('/eliminar_clients/<id>', methods=['GET'])
def eliminar(id):
    clientes= clients.query.get(id)
    db.session.delete(clientes)
    db.session.commit()
    return jsonify(clientesSchema.dump(clientes))

@app.route('/actualizar_clients', methods=['POST'])
def actualizar():
    id= request.json['id']
    datos= request.json['full_name','telefono','direccion','email','password']
    clientes= clients.query.get(id)
    clientes.datos= datos
    db.session.commit()
    return redirect('/clients') 

@app.route('/guardar_clients',methods= ['POST'])
def guardar():
    addclient= request.json['full_name','telefono','direccion','email','password']
    print(addclient)
    new_client= clients(addclient)
    db.session.add(new_client)
    db.session.commit()
    return redirect('/clients')

#token
@routes_clients.route('/obtenerToken', methods=['GET'])
def obtenertoken():
    #var_request = json.loads(event["body"])   
    datatoken = generar_token("cam", 123)
    var_Token = datatoken["token"]
    response = {"statusCode": 200, "body": json.dumps(var_Token)}    
    return response

@routes_clients.route('/verificartoken', methods=['GET'])
def verificartoken():
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    print("token =>", token)
      # Call the function to validate token
    vf = verificar_token(token)
    print("vf =>", vf)
    return vf