from config.db import db, app, ma 

class report(db.Model):
    __tableame__= "tbl_reports"
    
    
    id= db.Column(db.Integer, primary_key= True)
    id_cliente= db.Column(db.Integer, db.Foreignkey("tbl_clients.id"))
    id_pc= db.Column(db.Integer, db.Foreignkey("tbl_pcs.id"))
    programas_install= db.Column(db.String(200))
    observaciones= db.Column(db.String(200))
    estado= db.Column(db.String(200))
    fecha_inicio= db.Column(db.Date)
    fecha_fin= db.Column(db.Date)
    
    
    
    def __init__(self,id_cliente,id_pc,programas_install,observaciones,estado,fecha_inicio ,fecha_fin):
        self.id_cliente= id_cliente 
        self.id_pc= id_pc
        self.programas_install= programas_install
        self.observaciones= observaciones
        self.estado= estado
        self.fecha_inicio= fecha_inicio
        self.fecha_fin= fecha_fin
        
        
        with app.app_context():
            db.create_all()

class reportsSchema(ma.Schema):
    class Meta:
        fields= ('id','id_cliente','id_pc','programas_install','observaciones','estado','fecha_inicio','fecha_fin')