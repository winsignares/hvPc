from config.db import db, app, ma 

class generos(db.Model):
    __tablename__= "tbl_generos"
    
    
    id= db.Column(db.Integer, primary_key= True)
    genero= db.Column(db.String(200))
    
    
    
    def __init__(self,genero):
        self.genero= genero
    
        
        
        
with app.app_context():
    db.create_all()

class generosSchema(ma.Schema):
    class Meta:
        fields= ('id','genero')