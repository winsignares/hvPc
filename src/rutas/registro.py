from config.db import db, app, ma
from flask import Blueprint,render_template

routes_register= Blueprint("routes_register",__name__)

@routes_register.route("/indexregistro", methods= ["GET"])
def indexregistro():
    return render_template("/main/registro.html")

