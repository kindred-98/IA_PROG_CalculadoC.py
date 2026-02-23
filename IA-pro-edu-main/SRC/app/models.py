from app.extensions import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    
    operaciones = db.relationship("Operacion", backref="usuario", lazy=True)

class Operacion(db.Model):
    __tablename__ = "operaciones"

    id = db.Column(db.Integer, primary_key=True)
    expresion = db.Column(db.String(200), nullable=False)
    resultado = db.Column(db.String(50), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

    def __repr__(self):
        return f"<Operacion {self.expresion} = {self.resultado}>"