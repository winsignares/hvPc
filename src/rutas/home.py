from config.db import db, app, ma
from flask import Blueprint,render_template

routes_home= Blueprint("routes_home",__name__)

@routes_home.route("/indexhome", methods= ["GET"])
def indexregistro():
    return render_template("/main/home.html")