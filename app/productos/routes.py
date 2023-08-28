from app.productos import productos

@productos.route('/create')
def crear():
    return 'Aqui vamos a registrar productos'