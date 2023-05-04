from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#rutas de las tablas 
from api.clients import routes_clients
from api.pcs import routes_pcs
from api.reports import route_reports
from api.admin import routes_admin
#rutas de los htmls
from rutas.registro import routes_register
from rutas.login import routes_login



#ubicacion de las apis 
app.register_blueprint(routes_clients, url_prefix="/api")
app.register_blueprint(routes_pcs, url_prefix="/api")
app.register_blueprint(route_reports, url_prefix="/api")
app.register_blueprint(routes_admin, url_prefix="/api")

#ubicacion de la ruta
app.register_blueprint(routes_register, url_prefix="/fronted")
app.register_blueprint(routes_login, url_prefix="/fronted")

@app.route("/")
def index():
    titulo= "pagina principal"
    return render_template("/main/login.html", titles= titulo)

if __name__=="__main__":
    app.run(debug=True, port=5000, host= '0.0.0.0')

