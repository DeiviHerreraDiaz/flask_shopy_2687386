from app.productos import productos
from flask import render_template
from .forms  import NewProductForm
import app
import os


@productos.route('/crear',  methods = ['GET', 'POST'])
def crear():        
        producto = app.models.Producto()
        form = NewProductForm()
        if form.validate_on_submit():
            # Guarda el producto en la bd
            form.populate_obj(producto),
            producto.imagen = form.Imagen.data.filename
            app.db.session.add(producto),
            app.db.session.commit()
            #Subir imagen a /imagenes
            archivo = form.Imagen.data 
            archivo.save(os.path.abspath(os.getcwd() + "\\app\\productos\\imagenes\\"+ producto.imagen))
            return render_template('crear.html', form = form)
        return render_template('crear.html', form = form)

@productos.route('/editar')
def editar():
    return 'Aquí vamos a editar productos'

@productos.route('/listar')
def listar():
    return 'Aquí vamos a listar productos'

@productos.route('/eliminar')
def eliminar():
    return 'Aquí vamos a eliminar productos'

