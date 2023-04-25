from common.token import *
from config.db import db,ma,app
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
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