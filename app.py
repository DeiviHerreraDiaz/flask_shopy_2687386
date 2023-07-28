# Dependecnias del proyecto
from flask import Flask
from config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

# Iniciar el objeto de SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelos - entidades del proyecto
class Cliente(db.Model):
    __tablename__ = "Clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(100), unique = True)
    
# class ():
#     hola = str