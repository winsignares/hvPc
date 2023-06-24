from config.db import db, app, ma
from flask import Blueprint,render_template,request,jsonify,session
from model.admin import admin,adminSchema
from common.token import *
routes_home= Blueprint("routes_home",__name__)

@routes_home.route("/indexhome", methods= ["GET"])
def indexregistro():
    return render_template("/main/home.html")


@routes_home.route('/checktoken', methods=['GET'])
def checktoken():
    id = session.get('id')
    if id:
        user = admin.query.get(id)

        if user:
            print('Token Expiration:', user.token_expiration)
            now = datetime.now()
            print('Current Datetime:', now)

            if user.token == request.headers.get('Authorization')[7:]:
                if user.is_token_valid():
                    print('Is Token Valid: True')
                    return jsonify({'token_expired': False}), 200

                # Token expired or does not exist, remove it from the user object
                user.token = None
                user.token_expiration = None
                db.session.commit()  # Confirmar los cambios en la base de datos
                print('Token deleted from user object')

    print('Is Token Valid: False')
    return jsonify({'token_expired': True}), 401