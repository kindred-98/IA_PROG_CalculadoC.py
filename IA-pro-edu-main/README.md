🧮 Calculadora Básica en Python
📌 Descripción

Este proyecto es una calculadora sencilla desarrollada en Python que permite realizar operaciones matemáticas básicas:

Suma
Resta
Multiplicación
División (con validación de división por cero)


# ==========================================
# Calculadora básica en Python
# Permite sumar, restar, multiplicar y dividir
# ==========================================

def calcular(num1, num2, operacion):
    """
    Realiza una operación matemática básica entre dos números.

    Parámetros:
        num1 (int | float): Primer número
        num2 (int | float): Segundo número
        operacion (str): Operación a realizar ("+", "-", "*", "/")

    Retorna:
        Resultado de la operación o mensaje de error.
    """
# Suma
    if operacion == "+":
        return num1 + num2

# Resta
    elif operacion == "-":
        return num1 - num2

# Multiplicación
    elif operacion == "*":
        return num1 * num2
        
# División (validando que no sea división por cero)
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: No se puede dividir entre 0"

    else:
        # En caso de que el usuario ingrese una operación no válida
        return "Operación no válida"



# ==========================================
# Bloque principal del programa
# Solo se ejecuta si el archivo se corre directamente
# ==========================================
if __name__ == "__main__":

# Solicita datos al usuario
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    operacion = input("Escribe '+', '-', '*' o '/': ")

# Llama a la función calcular
    resultado = calcular(num1, num2, operacion)

# Muestra el resultado
    print("El resultado es:", resultado)
