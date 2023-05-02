from config.db import db, app, ma 

class pc(db.Model):
    __tablename__= "tbl_pcs"
    
    
    id= db.Column(db.Integer, primary_key= True)
    marca= db.Column(db.String(200))
    serie= db.Column(db.Integer)
    capacidad_Ram= db.Column(db.String(200))
    tarjeta_grafica= db.Column(db.String(200))
    capacidad_discoDuro= db.Column(db.String(200))
    procesador= db.Column(db.String(200))
    sistema_operativo= db.Column(db.String(200))
    fecha_adquisicion= db.Column(db.Date)
    
    
    def __init__(self,marca,serie,capacidad_Ram,tarjeta_grafica,capacidad_discoDuro, procesador,sistema_operativo,fecha_adquisicion):
        self.marca= marca 
        self.serie= serie
        self.capacidad_Ram= capacidad_Ram
        self.tarjeta_grafica= tarjeta_grafica
        self.capacidad_discoDuro= capacidad_discoDuro
        self.procesador= procesador
        self.sistema_operativo= sistema_operativo
        self.fecha_adquisicion= fecha_adquisicion
        
with app.app_context():
    db.create_all()

class pcsSchema(ma.Schema):
    class Meta:
        fields= ('id','marca','serie','capacidad_Ram','tarjeta_grafica','capacidad_discoDuro','procesador','sistema_operativo','fecha_adquisicion')