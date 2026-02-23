from flask import Blueprint, render_template, request, redirect, url_for
from app.calculator import calcular

main = Blueprint("main", __name__)

# Historial en memoria (de momento)
historial = []


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

            historial.append(f"{num1} {operacion} {num2} = {resultado}")

        except Exception:
            valor_display = "Error"

    return render_template(
        "index.html",
        resultado=resultado,
        valor_display=valor_display,
        historial=historial
    )


@main.route("/borrar", methods=["POST"])
def borrar_historial():
    historial.clear()
    return redirect(url_for("main.inicio"))