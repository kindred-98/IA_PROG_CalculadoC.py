from app import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    db.create_all()
    
#TEMPORAL
# 🔍 Ver tablas existentes (modo moderno)
    inspector = db.inspect(db.engine)
    print("Tablas en la BD:", inspector.get_table_names())

if __name__ == "__main__":
    app.run(debug=True)