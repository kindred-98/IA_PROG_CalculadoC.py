from flask import Blueprint, render_template, request, redirect, url_for

# 🔹 NUEVO: importamos db y modelos
from app import db
from app.models import Operacion, Usuario

from app.calculator import calcular

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None
    valor_display = ""

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

            # 🔹 NUEVO: buscar o crear usuario
            usuario = Usuario.query.first()

            if not usuario:
                usuario = Usuario(nombre="Angel")
                db.session.add(usuario)
                db.session.commit()

            # 🔹 NUEVO: guardar operación en base de datos
            nueva_operacion = Operacion(
                expresion=f"{num1} {operacion} {num2}",
                resultado=valor_display,
                usuario_id=usuario.id
            )

            db.session.add(nueva_operacion)
            db.session.commit()

        except Exception:
            valor_display = "Error"

    # 🔹 NUEVO: obtener historial desde la base de datos
    operaciones = Operacion.query.order_by(Operacion.id.desc()).all()

    return render_template(
        "index.html",
        resultado=resultado,
        valor_display=valor_display,
        historial=operaciones  # 🔹 CAMBIADO
    )


@main.route("/borrar", methods=["POST"])
def borrar_historial():

    # 🔹 NUEVO: borrar todas las operaciones desde la BD
    Operacion.query.delete()
    db.session.commit()

    return redirect(url_for("main.inicio"))