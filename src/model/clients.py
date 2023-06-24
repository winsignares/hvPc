from config.db import db, app, ma 

class clients(db.Model):
    __tablename__ = "tbl_clients"
    
    
    id= db.Column(db.Integer, primary_key= True, autoincrement=False)
    full_name= db.Column(db.String(200))
    tipo_document= db.Column(db.String(200))
    telefono= db.Column(db.Integer)
    direccion= db.Column(db.String(200))
    id_genero= db.Column(db.Integer, db.ForeignKey('tbl_generos.id'))
   
    
    def __init__(self,id,full_name,tipo_document,telefono,direccion, id_genero):
        self.id= id
        self.full_name= full_name
        self.tipo_document= tipo_document
        self.telefono= telefono
        self.direccion=direccion
        self.id_genero= id_genero
        
with app.app_context():
    db.create_all()

class clientesSchema(ma.Schema):
    class Meta:
        fields= ('id','full_name','tipo_document','telefono','direccion','id_genero')