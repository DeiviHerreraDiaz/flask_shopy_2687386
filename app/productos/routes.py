from app.productos import productos
from flask import render_template
from .forms  import NewProductForm


@productos.route('/crear',  methods = ['GET', 'POST'])
def crear():
    form = NewProductForm()
    # if form.validate_on_submit():
    #     producto = Producto
    #     (
            
    #     )
    # db.session.add(producto)
    # db.session.commit()
    # form=form0
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

