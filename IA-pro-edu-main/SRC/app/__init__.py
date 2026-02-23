from flask import Flask
from app.extensions import db


def create_app():

    app = Flask(__name__,
                static_folder="../static",
                template_folder="../templates")

    # 🔥 Configuración SQLite
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///adcalcsci.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializar base de datos
    db.init_app(app)

# 🔥 IMPORTAR MODELOS PARA QUE SQLALCHEMY LOS DETECTE
    from app import models

    from app.routes import main
    app.register_blueprint(main)

    return app