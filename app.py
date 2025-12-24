from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from config import Config
from modelos import db, Usuario  # models renombrado a modelos.py
from rutas.contacto import contacto_bp
from rutas.usuario import usuario_bp
from rutas.reserva import reserva_bp

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gimnasio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB
db.init_app(app)

# Inicializar Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "usuario.login"

# Función para cargar usuarios
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Inicializar Mail
mail = Mail(app)

# Registrar blueprints
app.register_blueprint(usuario_bp)
app.register_blueprint(reserva_bp)
app.register_blueprint(contacto_bp)

@app.route("/")
def index():
    return render_template("index.html")

# Crear tablas y correr app
if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all()
            print("Base de datos creada correctamente")
        except Exception as e:
            print("Error creando la base de datos:", e)
    app.run(debug=True)
