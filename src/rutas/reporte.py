from config.db import db, app, ma
from flask import Blueprint,render_template, request
from model.clients import clients
from model.pc import pc
routes_report= Blueprint("routes_report",__name__)

@routes_report.route("/indexreport", methods= ["GET"])
def indexregistro():
    return render_template("/main/reporte.html")


@routes_report.route('/guardar_cliente', methods= ["POST"])
def savecliente():
    full_name = request.form['full_name'] 
    tipo_document = request.form['tipo_document']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    id_genero = request.form['id_genero']
    print(full_name)
    new_client = clients(full_name,tipo_document,telefono,direccion,id_genero)
    db.session.add(new_client)
    db.session.commit()
    return "ok"

@routes_report.route('/guardar_pcs', methods= ["POST"])
def savepcs():
    marca= request.form['marca'] 
    serie = request.form['serie']
    capacidad_Ram = request.form['capacidad_Ram']
    tarjeta_grafica = request.form['tarjeta_grafica']
    capacidad_discoDuro = request.form['capacidad_discoDuro']
    procesador = request.form['procesador']
    sistema_operativo = request.form['sistema_operativo']
    fecha_adquisicion = request.form['fecha_adquisicion']
    print(marca)
    new_pc = clients(marca,serie,capacidad_Ram,tarjeta_grafica,capacidad_discoDuro,procesador,sistema_operativo,fecha_adquisicion)
    db.session.add(new_pc)
    db.session.commit()
    return "ok"