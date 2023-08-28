from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class NewProductForm(FlaskForm):
    nombre = StringField("NOMBRE PRODUCTO")
    precio = IntegerField("PRECIO PRODUCTO")
    submit = SubmitField("GUARDAR")
