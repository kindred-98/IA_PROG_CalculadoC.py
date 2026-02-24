from flask import Blueprint, render_template, request, redirect, url_for, session

from app import db
from app.models import Operacion, Usuario
from app.calculator import calcular

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None
    valor_display = ""

    # 🔹 Obtener usuario desde sesión (si existe)
    usuario_id = session.get("user_id")

    if request.method == "POST":
        num1 = request.form.get("num1", "")
        num2 = request.form.get("num2", "")
        operacion = request.form.get("operacion", "")

        try:
            n1 = float(num1) if num1 else 0
            n2 = float(num2) if num2 else 0

            resultado = calcular(n1, n2, operacion)

            if isinstance(resultado, (int, float)):
                valor_display = f"{resultado:.10f}".rstrip('0').rstrip('.')
            else:
                valor_display = resultado

            # 🔥 SOLO guardar si hay usuario logueado
            if usuario_id:
                nueva_operacion = Operacion(
                    expresion=f"{num1} {operacion} {num2}",
                    resultado=valor_display,
                    usuario_id=usuario_id
                )

                db.session.add(nueva_operacion)
                db.session.commit()

        except Exception:
            valor_display = "Error"

    # 🔹 Mostrar historial solo si hay usuario logueado
    if usuario_id:
        operaciones = Operacion.query.filter_by(usuario_id=usuario_id)\
                                     .order_by(Operacion.id.desc()).all()
    else:
        operaciones = []

    return render_template(
        "index.html",
        resultado=resultado,
        valor_display=valor_display,
        historial=operaciones
    )


@main.route("/borrar", methods=["POST"])
def borrar_historial():

    usuario_id = session.get("user_id")

    if usuario_id:
        Operacion.query.filter_by(usuario_id=usuario_id).delete()
        db.session.commit()

    return redirect(url_for("main.inicio"))