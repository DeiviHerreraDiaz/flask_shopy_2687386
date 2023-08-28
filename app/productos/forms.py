from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField 

class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese el nombre del producto")
    precio = IntegerField("Ingrese el precio del producto")
    Imagen = StringField("Ingrese la imágen del producto")
    submit = SubmitField("Crear")
    
    