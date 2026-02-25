from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.models import Operacion, Usuario
from app.calculator import calcular

main = Blueprint("main", __name__)


# ==========================================================
# 🔐 REGISTER
# Permite crear una nueva cuenta de usuario
# ==========================================================
@main.route("/register", methods=["POST"])
def register():

    username = request.form.get("username")
    email = request.form.get("email").lower()
    password = request.form.get("password")

    # 🔹 Verificar si ya existe usuario o email
    user_exists = Usuario.query.filter(
        (Usuario.username == username) | (Usuario.email == email)
    ).first()

    if user_exists:
        flash("Usuario o email ya existen")
        return redirect(url_for("main.inicio"))

    # 🔹 Encriptar contraseña
    password_hash = generate_password_hash(password)

    # 🔹 Crear usuario
    nuevo_usuario = Usuario(
        username=username,
        email=email,
        password_hash=password_hash
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    # 🔹 Crear sesión automáticamente tras registro
    session["user_id"] = nuevo_usuario.id

    return redirect(url_for("main.inicio"))


# ==========================================================
# 🔐 LOGIN
# Verifica credenciales y crea sesión
# ==========================================================
@main.route("/login", methods=["POST"])
def login():

    email = request.form.get("email").lower()
    password = request.form.get("password")

    # 🔹 Buscar usuario por email
    usuario = Usuario.query.filter_by(email=email).first()

    if not usuario:
        flash("Usuario no encontrado")
        return redirect(url_for("main.inicio"))

    # 🔹 Verificar contraseña hasheada
    if not check_password_hash(usuario.password_hash, password):
        flash("Contraseña incorrecta")
        return redirect(url_for("main.inicio"))

    # 🔹 Guardar ID en sesión
    session["user_id"] = usuario.id

    return redirect(url_for("main.inicio"))


# ==========================================================
# 🧮 INICIO (CALCULADORA)
# Permite usar la calculadora con o sin login
# Guarda historial SOLO si el usuario está logueado
# ==========================================================
@main.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None
    valor_display = ""

    # 🔹 Obtener usuario logueado (si existe)
    usuario = None
    if "user_id" in session:
        usuario = Usuario.query.get(session["user_id"])

    # ======================================================
    # 🔹 SI SE ENVÍA OPERACIÓN
    # ======================================================
    if request.method == "POST":

        num1 = request.form.get("num1", "")
        num2 = request.form.get("num2", "")
        operacion = request.form.get("operacion", "")

        try:
            # Convertir a float (si están vacíos → 0)
            n1 = float(num1) if num1 else 0
            n2 = float(num2) if num2 else 0

            # Ejecutar cálculo
            resultado = calcular(n1, n2, operacion)

            # Formatear resultado
            if isinstance(resultado, (int, float)):
                valor_display = f"{resultado:.10f}".rstrip("0").rstrip(".")
            else:
                valor_display = resultado

            # ==================================================
            # 🔹 SOLUCIÓN CORRECTA:
            # Guardar SOLO si usuario está logueado
            # ==================================================
            if usuario:
                nueva_operacion = Operacion(
                    expresion=f"{num1} {operacion} {num2}",
                    resultado=valor_display,
                    usuario_id=usuario.id
                )

                db.session.add(nueva_operacion)
                db.session.commit()

        except Exception:
            valor_display = "Error"

    # ======================================================
    # 🔹 CARGAR HISTORIAL SOLO SI ESTÁ LOGUEADO
    # ======================================================
    if usuario:
        operaciones = Operacion.query.filter_by(
            usuario_id=usuario.id
        ).order_by(Operacion.id.desc()).all()
    else:
        operaciones = []

    return render_template(
        "index.html",
        resultado=resultado,
        valor_display=valor_display,
        historial=operaciones,
        usuario=usuario
    )


# ==========================================================
# 🔓 LOGOUT
# Elimina sesión y vuelve a la calculadora
# ==========================================================
@main.route("/logout")
def logout():

    session.pop("user_id", None)

    return redirect(url_for("main.inicio"))


# ==========================================================
# 🗑 BORRAR HISTORIAL
# Borra SOLO operaciones del usuario logueado
# ==========================================================
@main.route("/borrar", methods=["POST"])
def borrar_historial():

    if "user_id" not in session:
        return redirect(url_for("main.inicio"))

    Operacion.query.filter_by(
        usuario_id=session["user_id"]
    ).delete()

    db.session.commit()

    return redirect(url_for("main.inicio"))