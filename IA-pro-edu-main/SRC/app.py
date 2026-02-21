import os
from flask import Flask, redirect, request, url_for, render_template
import math

app = Flask(__name__, static_folder="static", template_folder="templates")

# Historial en memoria
historial = []


# =========================
# FUNCIÓN CALCULAR
# =========================
def calcular(num1, num2, operacion):

    if operacion == "+":
        return num1 + num2

    elif operacion == "-":
        return num1 - num2

    elif operacion == "*":
        return num1 * num2

    elif operacion == "/":
        return num1 / num2 if num2 != 0 else "Error: división por cero"

    elif operacion == "^":
        return num1 ** num2

    elif operacion == "√":
        return math.sqrt(num1) if num1 >= 0 else "Error: raíz negativa"

    elif operacion == "sin":
        return math.sin(num1)

    elif operacion == "cos":
        return math.cos(num1)

    elif operacion == "log":
        return math.log(num1) if num1 > 0 else "Error: log inválido"

    elif operacion == "exp":
        return math.exp(num1)

    else:
        return "Operación no válida"


# =========================
# RUTA PRINCIPAL
# =========================
@app.route("/", methods=["GET", "POST"])
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

            if operacion == "+":
                resultado = n1 + n2
            elif operacion == "-":
                resultado = n1 - n2
            elif operacion == "*":
                resultado = n1 * n2
            elif operacion == "/":
                resultado = n1 / n2
            elif operacion == "sin":
                resultado = math.sin(n1)
            elif operacion == "cos":
                resultado = math.cos(n1)
            elif operacion == "log":
                resultado = math.log10(n1)
            elif operacion == "√":
                resultado = math.sqrt(n1)
            elif operacion == "^":
                resultado = n1 ** n2
            elif operacion == "exp":
                resultado = math.exp(n1)

            valor_display = f"{resultado:.10f}".rstrip('0').rstrip('.')
            historial.append(f"{num1} {operacion} {num2} = {resultado}")

        except Exception:
            valor_display = "Error"

    return render_template(
        "index.html",
        resultado=resultado,
        valor_display=valor_display,
        historial=historial
    )

# =========================
# BORRAR HISTORIAL
# =========================
@app.route("/borrar", methods=["POST"])
def borrar_historial():
    historial.clear()
    return redirect(url_for("inicio"))

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)
