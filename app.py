# Dependecnias del proyecto
from flask import Flask
from config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Config)

# Iniciar el objeto de SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelos - entidades del proyecto
class Cliente(db.Model):
    __tablename_ = "clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique = True)

class Producto(db.Model):
    __tablename_ = "productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), unique = True)
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(10), unique = True)

class Venta(db.Model):
    __tablename_ = "ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha_venta = db.Column(db.DateTime, default= datetime.utcnow)    
    id_cliente = db.Column(db.Integer, db.ForeignKey(Producto.id))
#    productos = db.relationship('productos', secondary=post_tag, backref='ventas')
