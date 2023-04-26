from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#rutas de las tablas 
from api.clients import routes_clients
from api.pcs import routes_pcs
from api.reports import route_reports

#rutas de los htmls





#ubicacion de las apis 
app.register_blueprint(routes_clients, url_prefix="/api")
app.register_blueprint(routes_pcs, url_prefix="/api")
app.register_blueprint(route_reports, url_prefix="/api")

#ubicacion de la ruta





