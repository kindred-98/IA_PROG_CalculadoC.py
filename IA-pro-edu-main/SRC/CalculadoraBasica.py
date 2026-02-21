import math

def calcular(num1, num2, operacion):

    if operacion == "+":
        return num1 + num2

    elif operacion == "-":
        return num1 - num2

    elif operacion == "*":
        return num1 * num2

    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: No se puede dividir entre 0"

    # Potencia
    elif operacion == "^":
        return num1 ** num2

    # Raíz cuadrada (solo usa num1)
    elif operacion == "√":
        if num1 >= 0:
            return math.sqrt(num1)
        else:
            return "Error: raíz de número negativo"

    # Seno
    elif operacion == "sin":
        return math.sin(num1)

    elif operacion == "cos":
        return math.cos(num1)

    # Logaritmo
    elif operacion == "log":
        if num1 > 0:
            return math.log(num1)
        else:
            return "Error: logaritmo de número no positivo"

    else:
        return "Operación no válida"


# =========================
# MENÚ INTERACTIVO
# =========================

while True:
    print("\n=== CALCULADORA CIENTÍFICA ===")
    print("Operaciones básicas: +  -  *  /")
    print("Científicas: ^  √  sin  cos  log")
    print("Escribe 'salir' para terminar")

    operacion = input("Elige una operación: ")

    if operacion.lower() == "salir":
        print("¡Hasta luego!")
        break

    # Operaciones que solo usan un número
    if operacion in ["√", "sin", "cos", "log"]:
        num1 = float(input("Ingresa el número: "))
        num2 = 0  # no se usa, pero mantenemos la función igual

    else:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

    resultado = calcular(num1, num2, operacion)
    print("Resultado:", resultado)