# Dependecnias del proyecto
from flask import Flask, render_template
from config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField



# Iniciar objeto Flask

app = Flask(__name__)
app.config.from_object(Config)

# Iniciar el objeto de SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Crear el formulario de registro de Cliente

class RegistroClienteForm(FlaskForm):
    username =  StringField("Nombre del Usuario")
    email =   StringField("Email del Usuario")
    password = PasswordField("Password del Usuario")
    submit = SubmitField("Registrar")

# Modelos - entidades del proyecto
class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique = True)

class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), unique = True)
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(10), unique = True)

class Venta(db.Model):
    __tablename__ = "ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha_venta = db.Column(db.DateTime, default= datetime.utcnow)    
    cliente_id = db.Column(db.Integer, 
                           db.ForeignKey('clientes.id'))
    
class Detalle(db.Model):
    __tablename__ = "detalles"
    id = db.Column(db.Integer, primary_key = True)
    producto_id = db.Column(db.Integer, 
                           db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, 
                            db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)

@app.route('/clientes/create', methods = ['GET', 'POST'])
def crear_cliente():
    form = RegistroClienteForm()
    if form.validate_on_submit():
        # Crear el cliente
        cliente = Cliente(username = form.username.data, 
                          email =form.email.data,
                          password = form.password.data)
        db.session.add(cliente)
        db.session.commit()
        return "registro de cliente"
    return render_template('registro.html', 
                           form = form)

@app.route('/clientes', 
           methods=['GET'])
def listar():
    clientes = Cliente.query.all()
    return render_template('listar.html',
                           clientes = clientes)