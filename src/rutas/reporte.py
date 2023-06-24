from config.db import db, app, ma
from flask import Blueprint,render_template, request, jsonify
from model.clients import clients
from model.pc import pc
from model.reports import report
from model.admin import admin
routes_report= Blueprint("routes_report",__name__)

@routes_report.route("/indexreport", methods= ["GET"])
def indexregistro():
    return render_template("/main/reporte.html")


@routes_report.route('/guardar_cliente', methods= ["POST"])
def savecliente():
    id= request.form['id']
    full_name = request.form['full_name'] 
    tipo_document = request.form['tipo_document']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    id_genero = request.form['id_genero']
    print(full_name)
    new_client = clients(id,full_name,tipo_document,telefono,direccion,id_genero)
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
    new_pc = pc(marca,serie,capacidad_Ram,tarjeta_grafica,capacidad_discoDuro,procesador,sistema_operativo,fecha_adquisicion)
    db.session.add(new_pc)
    db.session.commit()
    return "ok"



@routes_report.route('/guardar_reports', methods= ["POST"])
def savereports():
    id= request.form['id']
    id_cliente= request.form['id_cliente'] 
    id_pc = request.form['id_pc']
    id_admin = request.form['id_admin']
    programas_install = request.form['programas_install']
    observaciones = request.form['observaciones']
    estado = request.form['estado']
    fecha_inicio = request.form['fecha_inicio']
    fecha_fin = request.form['fecha_fin']
    print(id_cliente)
    new_reports = report(id,id_cliente,id_pc,id_admin,programas_install,observaciones,estado,fecha_inicio,fecha_fin)
    db.session.add(new_reports)
    db.session.commit()
    return "ok"


@routes_report.route('/obtenerNombre/<id>', methods=['GET'])
def obtener_nombre_por_id(id):
   
    dato = report.query.filter_by(id_admin=id).first()

    if dato:
        relacion= admin.query.filter_by(id=dato.id_admin).first()
       
    
    if relacion:
        return jsonify({'full_name': relacion.full_name})
    else:
        # Si no se encuentra el ID, devolver una respuesta vacía
        return jsonify({})




@routes_report.route('/obtenerClients/<id>', methods=['GET'])
def obtener_clientes_id(id):
   clientes= clients.query.get(id)
   
   if clientes is None:
       return jsonify({"error": 'id no encontrado'})
   data ={
       'id': clientes.id,
       'full_name': clientes.full_name,
       'tipo_document': clientes.tipo_document,
       'telefono': clientes.telefono,
       'direccion': clientes.direccion
    }
   return jsonify(data)
           
       
@routes_report.route('/obtenerPcs/<id>', methods=['GET'])
def obtener_pcs_id(id):
   pcs= pc.query.get(id)
   
   if pcs is None:
       return jsonify({"error": 'id no encontrado'})
   data ={
       
       'id': pcs.id,
       'marca': pcs.marca,
       'serie': pcs.serie,
       'capacidad_Ram': pcs.capacidad_Ram,
       'tarjeta_grafica': pcs.tarjeta_grafica,
       'capacidad_discoDuro': pcs.capacidad_discoDuro,
       'procesador': pcs.procesador,
       'sistema_operativo': pcs.sistema_operativo,
       'fecha_adquisicion': pcs.fecha_adquisicion
    }
   return jsonify(data)      
   
  
@routes_report.route('/obtenerReports/<id>', methods=['GET'])
def obtener_reports_id(id):
   reports= report.query.get(id)
   
   if reports is None:
       return jsonify({"error": 'id no encontrado'})
   data ={
       
       'observaciones': reports.observaciones,
       'programas_install': reports.programas_install,

       'estado': reports.estado,
       'fecha_inicio': reports.fecha_inicio,
       'fecha_fin': reports.fecha_fin
    }
   return jsonify(data)
           