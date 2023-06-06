from common.token import *
from config.db import db,ma,app
from flask import Flask, Blueprint, redirect, request, jsonify, json, session
from model.reports import report,reportsSchema

#ruta de reportes
route_reports= Blueprint('routes_reports',__name__)

report_Schema= reportsSchema()
reports_Schema= reportsSchema(many= True)

#crud reports
app.route('/reports', methods=['GET'])
def reports():
    returnall= report.query.all()
    result_report= reports_Schema.dump(returnall)
    return jsonify(result_report)

app.route('/eliminar_reports/<id>', methods=['GET'])
def eliminar_reports(id):
    reports= report.query.get(id)
    db.session.delete(reports)
    db.sessio.commit()
    return jsonify(reportsSchema.dump(reports))

app.route('/actualizar_reports',methods=['POST'])
def actualizar_reports():
    id= request.json['id']
    datos= request.json['id_cliente','id_pc','programas_install','observaciones','estado','fecha_inicio','fecha_fin']
    reports= report.query.get(id)
    reports.datos= datos
    db.session.commit()
    return redirect('/reports')

app.route('/guardar_reports',methods=['POST'])
def guardar_reports():
    addreports= request.json['id_cliente','id_pc','programas_install','observaciones','estado','fecha_inicio','fecha_fin']
    print(addreports)
    newreport= report(addreports)
    db.session.add(newreport)
    db.session.commit()
    return redirect('/reports')





