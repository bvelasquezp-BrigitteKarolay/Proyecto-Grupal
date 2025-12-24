from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# -------------------------------
# Modelo de Usuario
# -------------------------------
class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), default="usuario")  # "usuario" o "admin"

    reservas = db.relationship("Reserva", backref="usuario", lazy=True)

    def __repr__(self):
        return f"<Usuario {self.nombre} - {self.rol}>"

# -------------------------------
# Modelo de Reserva
# -------------------------------
class Reserva(db.Model):
    __tablename__ = "reservas"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    recurso = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    hora = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Reserva {self.recurso} - {self.fecha} {self.hora}>"

# -------------------------------
# Modelo de Contacto
# -------------------------------
class Contacto(db.Model):
    __tablename__ = "contactos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    mensaje = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Contacto {self.nombre} - {self.email}>"
