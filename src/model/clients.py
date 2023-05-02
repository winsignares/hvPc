from config.db import db, app, ma 

class clients(db.Model):
    __tablename__= "tbl_clients"
    
    
    id= db.Column(db.Integer, primary_key= True)
    full_name= db.Column(db.String(200))
    telefono= db.Column(db.Integer)
    direccion= db.Column(db.String(200))
    
    
    def __init__(self,full_name,telefono,direccion):
        self.full_name= full_name
        self.telefono= telefono
        self.direccion=direccion
        
        
with app.app_context():
    db.create_all()

class clientesSchema(ma.Schema):
    class Meta:
        fields= ('id','full_name','telefono','direccion')