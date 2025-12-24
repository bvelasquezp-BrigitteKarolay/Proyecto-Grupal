from flask import Blueprint, render_template, request, flash, redirect, url_for
from modelos import db, Contacto

contacto_bp = Blueprint("contacto", __name__, template_folder="../templates")

@contacto_bp.route("/contactanos", methods=["GET", "POST"])
def contactanos():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        telefono = request.form.get("telefono")
        mensaje = request.form.get("mensaje")

        nuevo_contacto = Contacto(
            nombre=nombre,
            email=email,
            telefono=telefono,
            mensaje=mensaje
        )
        db.session.add(nuevo_contacto)
        db.session.commit()

        flash("Mensaje enviado con éxito", "success")
        return redirect(url_for("contacto.contactanos"))

    return render_template("contactanos.html")
