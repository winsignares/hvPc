from config.db import db, app, ma
from flask import Blueprint,render_template

routes_login= Blueprint("routes_login",__name__)

@routes_login.route("/indexlogin", methods= ["GET"])
def indexregistro():
    return render_template("/main/login.html")