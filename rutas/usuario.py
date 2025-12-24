from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from modelos import db, Usuario


usuario_bp = Blueprint('usuario', __name__, template_folder='../templates')

# Registro de usuario
@usuario_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        password = request.form.get("password")

        if Usuario.query.filter_by(email=email).first():
            flash("Este correo ya está registrado.", "danger")
            return redirect(url_for("usuario.registro"))

        nuevo_usuario = Usuario(
            nombre=nombre,
            email=email,
            password=generate_password_hash(password),
            rol="usuario"
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash("Usuario registrado correctamente.", "success")
        return redirect(url_for("usuario.login"))

    return render_template("registro.html")

# Login
@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario or not check_password_hash(usuario.password, password):
            flash("Correo o contraseña incorrectos.", "danger")
            return redirect(url_for("usuario.login"))

        login_user(usuario)
        flash(f"Bienvenido {usuario.nombre}!", "success")
        return redirect(url_for("index"))

    return render_template("login.html")

# Logout
@usuario_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada correctamente.", "info")
    return redirect(url_for("index"))
