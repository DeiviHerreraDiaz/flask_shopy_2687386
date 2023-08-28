from flask import render_template
from app.productos import productos
from .forms import NewProductForm


# CREAR

@productos.route('/create')
def crear():
    
    form = NewProductForm()
    return render_template('new.html',
                           form = form)

# ELIMINAR

@productos.route('/delete')
def eliminar():
    return 'Vamos a eliminar'