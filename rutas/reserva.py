from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from modelos import db, Reserva

reserva_bp = Blueprint("reserva", __name__, template_folder="../templates")

@reserva_bp.route("/reserva", methods=["GET", "POST"])
@login_required  # Necesita estar logueado para reservar
def reserva():
    if request.method == "POST":
        recurso = request.form.get("clase")  # Nombre del select en el form
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")

        # Crear reserva asociada al usuario actual
        nueva_reserva = Reserva(
            usuario_id=current_user.id,
            recurso=recurso,
            fecha=fecha,
            hora=hora
        )
        db.session.add(nueva_reserva)
        db.session.commit()

        flash("Reserva creada con éxito", "success")
        return redirect(url_for("reserva.reserva"))

    return render_template("reserva.html")
