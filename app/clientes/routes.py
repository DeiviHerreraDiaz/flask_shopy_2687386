from app.clientes import clientes
from flask import render_template, redirect, flash
import app
from .forms import NewClientForm, EditClientForm



@clientes.route('/crear' ,  methods = ['GET', 'POST'])
def crear():
    
    cliente = app.models.Cliente()
    form = NewClientForm()
    if form.validate_on_submit():
        form.populate_obj(cliente),
        app.db.session.add(cliente),
        app.db.session.commit()
        flash("Cliente registrado correctamente")
        return redirect('/clientes/listar')
    return render_template('crearClient.html', form = form)

@clientes.route('/listar')
def listar():
    clientes = app.models.Cliente.query.all()    
    return render_template("listarClient.html",
                           clientes = clientes)

@clientes.route('/eliminar/<cliente_id>')
def eliminar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    if p:
        app.db.session.delete(p)
        app.db.session.commit()
        flash('Cliente eliminado')
    return redirect ('/clientes/listar')


@clientes.route('/editar/<cliente_id>', methods = ['GET', 'POST'])
def editar(cliente_id):
    
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClientForm(obj = p)
    
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Cliente actualizado')
        return redirect('/clientes/listar')
    return render_template("crearClient.html",
                           form = form)
        
    
