from app.extensions import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    operaciones = db.relationship("Operacion", backref="usuario", lazy=True)
    
class Operacion(db.Model):
    __tablename__ = "operaciones"

    id = db.Column(db.Integer, primary_key=True)
    expresion = db.Column(db.String(200), nullable=False)
    resultado = db.Column(db.String(50), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

    def __repr__(self):
        return f"<Operacion {self.expresion} = {self.resultado}>"