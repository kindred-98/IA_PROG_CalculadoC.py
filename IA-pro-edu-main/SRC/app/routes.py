from flask import Blueprint, render_template, request, redirect, url_for, session, flash

# 🔹 CAMBIO 1: añadimos generate y check hash
from werkzeug.security import generate_password_hash, check_password_hash

# 🔹 CAMBIO 2: importamos db y modelos
from app import db
from app.models import Operacion, Usuario
from app.calculator import calcular

main = Blueprint("main", __name__)


# ==============================
# 🔐 REGISTER
# ==============================
@main.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email").lower()
        password = request.form.get("password")

        # 🔹 CAMBIO 3: verificar si ya existe
        user_exists = Usuario.query.filter(
            (Usuario.username == username) | (Usuario.email == email)
        ).first()

        if user_exists:
            flash("Usuario o email ya existen")
            return redirect(url_for("main.register"))

        # 🔹 CAMBIO 4: hash contraseña
        password_hash = generate_password_hash(password)

        nuevo_usuario = Usuario(
            username=username,
            email=email,
            password_hash=password_hash
        )

        db.session.add(nuevo_usuario)
        db.session.commit()

        # 🔹 CAMBIO 5: guardar sesión
        session["user_id"] = nuevo_usuario.id

        return redirect(url_for("main.inicio"))

    # return render_template("register.html")


# ==============================
# 🔐 LOGIN
# ==============================
@main.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email").lower()
        password = request.form.get("password")

        # 🔹 CAMBIO 6: buscar usuario
        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario:
            flash("Usuario no encontrado")
            return redirect(url_for("main.login"))

        # 🔹 CAMBIO 7: verificar contraseña
        if not check_password_hash(usuario.password_hash, password):
            flash("Contraseña incorrecta")
            return redirect(url_for("main.login"))

        # 🔹 CAMBIO 8: crear sesión
        session["user_id"] = usuario.id

        return redirect(url_for("main.inicio"))

    # return render_template("login.html")


# ==============================
# 🧮 INICIO (PROTEGIDO)
# ==============================
@main.route("/", methods=["GET", "POST"])
def inicio():

    # # 🔹 CAMBIO 9: proteger ruta
    # if "user_id" not in session:
    #     return redirect(url_for("main.login"))
        
    resultado = None
    valor_display = ""

    # 🔹 CAMBIO 10: obtener usuario logueado
    usuario = None
    if "user_id" in session:
        usuario = Usuario.query.get(session["user_id"])

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

            # # 🔹 CAMBIO 11: guardar operación asociada al usuario
            # nueva_operacion = Operacion(
            #     expresion=f"{num1} {operacion} {num2}",
            #     resultado=valor_display,
            #     usuario_id=usuario.id
            # )

            # 🔹 SOLO guardamos en BD si está logueado
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

    # # 🔹 CAMBIO 12: mostrar SOLO operaciones del usuario
    # operaciones = Operacion.query.filter_by(
    #     usuario_id=usuario.id
    # ).order_by(Operacion.id.desc()).all()

     # 🔹 Mostrar historial solo si está logueado
    if usuario:
        operaciones = Operacion.query.filter_by(
            usuario_id=usuario.id
        ).order_by(Operacion.id.desc()).all()
    else:
        operaciones = []  # 🔹 Sin login → sin historial

    return render_template(
        "index.html",
        resultado=resultado,
        valor_display=valor_display,
        historial=operaciones,
        usuario=usuario
    )


# ==============================
# 🔓 LOGOUT
# ==============================

@main.route("/logout")
def logout():
    # 🔹 CAMBIO 13: cerrar sesión
    session.pop("user_id", None)

    # 🔹 Siempre vuelve a la calculadora
    return redirect(url_for("main.inicio"))


# ==============================
# 🗑 BORRAR HISTORIAL
# ==============================
@main.route("/borrar", methods=["POST"])
def borrar_historial():

# 🔹 Solo permitimos borrar si está logueado
    if "user_id" not in session:
        return redirect(url_for("main.login"))

    # 🔹 CAMBIO 14: borrar SOLO operaciones del usuario
    Operacion.query.filter_by(usuario_id=session["user_id"]).delete()

    db.session.commit()

    return redirect(url_for("main.inicio"))