from config.db import db, app, ma 
from common.token import *
import secrets
class admin(db.Model):
    __tablename__="tbl_admin"
    
    id= db.Column(db.Integer, primary_key= True)
    full_name= db.Column(db.String(200))
    telefono= db.Column(db.Integer)
    direccion= db.Column(db.String(200))
    email= db.Column(db.String(200))
    password= db.Column(db.String(200))
    id_genero= db.Column(db.Integer, db.ForeignKey('tbl_generos.id'))
    token= db.Column(db.String(200))
    token_expiration = db.Column(db.DateTime)
    
    def __init__(self,full_name,telefono,direccion,email,password,id_genero):
        self.full_name= full_name
        self.telefono= telefono
        self.direccion=direccion
        self.email= email
        self.password= password
        self.id_genero= id_genero

    def generate_token(self):
        self.token = secrets.token_hex(16)
        self.token_expiration = datetime.now() + timedelta(minutes=5)

    def is_token_valid(self):
        return datetime.now() <= self.token_expiration


with app.app_context():
    db.create_all()

class adminSchema(ma.Schema):
    class meta:
        fields= ('id','full_name','telefono','direccion','email','password','id_genero')
        
