import math

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
        return num1 / num2 if num2 != 0 else "No se puede divir entre 0"

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