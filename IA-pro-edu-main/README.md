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


# AdCalSci - Advanced Calculator Scientific

AdCalSci es una calculadora científica web desarrollada con Flask y
SQLite. El proyecto evolucionó desde una aplicación simple con historial
en memoria hasta una arquitectura backend modular con persistencia real
en base de datos.

## Tecnologías utilizadas

-   Python
-   Flask
-   Flask-SQLAlchemy
-   SQLite
-   HTML5
-   CSS3

## Arquitectura del proyecto

app/ │ ├── **init**.py → Inicialización de Flask y base de datos ├──
models.py → Modelos Usuario y Operacion ├── routes.py → Rutas
principales y lógica de guardado ├── calculator.py → Lógica matemática
separada │ templates/ │ └── index.html │ static/ │ └── style.css

## Funcionalidades actuales

-   Operaciones matemáticas básicas y científicas
-   Formateo de resultados (máximo 10 decimales)
-   Historial persistente en SQLite
-   Borrado completo del historial
-   Arquitectura modular profesional

## Conceptos backend aplicados

-   Separación de responsabilidades
-   Uso de Blueprint
-   Modelos relacionales con ForeignKey
-   db.session.add()
-   db.session.commit()
-   Persistencia de datos

## Estado actual

Aplicación funcional, estructurada profesionalmente y lista para escalar
con autenticación, API y despliegue en producción.

RESUMEN DE LO QUE CAMBIÓ
24/02/26
| Cambio | Qué hace                     |
| ------ | ---------------------------- |
| 1      | Import hash                  |
| 3      | Verificar duplicados         |
| 4      | Hashear contraseña           |
| 5      | Guardar sesión en register   |
| 6      | Buscar usuario login         |
| 7      | Validar contraseña           |
| 9      | Proteger inicio              |
| 10     | Obtener usuario logueado     |
| 11     | Asociar operación al usuario |
| 12     | Mostrar solo su historial    |
| 13     | Logout                       |
| 14     | Borrar solo su historial     |
