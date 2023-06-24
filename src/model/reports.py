from config.db import db, app, ma 

class report(db.Model):
    __tablename__ = "tbl_reports"
    
    
    id= db.Column(db.Integer, primary_key= True,  autoincrement=False)
    id_cliente= db.Column(db.Integer, db.ForeignKey("tbl_clients.id"))
    id_pc= db.Column(db.Integer, db.ForeignKey("tbl_pcs.id"))
    id_admin= db.Column(db.Integer, db.ForeignKey("tbl_admin.id"))
    programas_install= db.Column(db.String(200))
    observaciones= db.Column(db.String(200))
    estado= db.Column(db.String(200))
    fecha_inicio= db.Column(db.Date)
    fecha_fin= db.Column(db.Date)
    
    
    
    def __init__(self,id,id_cliente,id_pc,id_admin,programas_install,observaciones,estado,fecha_inicio ,fecha_fin):
        self.id=id
        self.id_cliente= id_cliente 
        self.id_pc= id_pc
        self.id_admin= id_admin
        self.programas_install= programas_install
        self.observaciones= observaciones
        self.estado= estado
        self.fecha_inicio= fecha_inicio
        self.fecha_fin= fecha_fin
        
        
with app.app_context():
    db.create_all()

class reportsSchema(ma.Schema):
    class Meta:
        fields= ('id','id_cliente','id_pc','id_admin','programas_install','observaciones','estado','fecha_inicio','fecha_fin')