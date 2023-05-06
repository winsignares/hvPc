from config.db import db, app, ma 

class admin(db.Model):
    __tablename__="tbl_admin"
    
    id= db.Column(db.Integer, primary_key= True)
    full_name= db.Column(db.String(200))
    telefono= db.Column(db.Integer)
    email= db.Column(db.String(200))
    password= db.Column(db.String(200))
    id_genero= db.Column(db.Integer, db.ForeignKey('tbl_generos.id'))
   
    
    def __init__(self,full_name,telefono,direccion,email,password,id_genero):
        self.full_name= full_name
        self.telefono= telefono
        self.direccion=direccion
        self.email= email
        self.password= password
        self.id_genero= id_genero


with app.app_context():
    db.create_all()

class adminSchema(ma.Schema):
    class meta:
        fields= ('id','full_name','telefono','direccion','email','password','id_genero')
        
