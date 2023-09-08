from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField 
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import *

class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese el nombre del producto", 
                         validators = [InputRequired( message = "llenalo chamo" )])
    precio = IntegerField("Ingrese el precio del producto",
                          validators = [InputRequired( message = "Decime el precio"),
                          NumberRange (min = 10000,
                                      max = 100000,
                                      message = "Bajale o Subile")])
    Imagen = FileField(label = "Imagen",
                       validators = [
                           FileRequired(message = "Ponga imagen marico"),
                            FileAllowed (
                                ["jpg","png"], 
                                message = "Formato invalido"
                            )
                       ])
    submit = SubmitField("Crear")
