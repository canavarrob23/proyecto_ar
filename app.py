from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import crud_prod
from forms import frm_producto
# from flask_wtf.csrf import CSRFProtect

# inicializa aplicacion
app = Flask(__name__)

#   settings
app.secret_key = 'miclavesecreta'

@app.route('/')
def home():
    return render_template('index.html')

# =================
@app.route('/crud', methods=["GET", "POST"])
def crud_producto():

    modo = request.args.get('modo',None)
    accion = request.form.get('accion',None)
    id = request.args.get('id',None)
    print('modo:', modo)
    print('accion:', accion)
    print('request.method ',request.method)

    if request.method == "GET":
        datos = crud_prod.get_productos()
        if id and id != None:
            dato  = crud_prod.sel_producto(id)
            print('dato:', dato)
            return render_template('crud_producto.html', productos=datos, prod=dato, modo=modo)
        else:
            return render_template('crud_producto.html', productos=datos, modo=modo)

    elif request.method == "POST":

        if accion=='ins':
            print('INSERT')
            datos = request.form
            print(datos)
            codiprod = datos["codiprod"]
            print(codiprod)
            prod  = crud_prod.get_producto(codiprod)
            print('prod ', prod)

            '''
            try:
                codiprod
                exist_prod = True
            except:
                exist_prod = False
            '''

            if codiprod and codiprod != None:
                prod  = crud_prod.get_producto(codiprod)

            if prod and prod != None:
                print('El producto ya existe')
                flash(f'El codigo de producto: ({codiprod}) ya esta REGISTRADO ...!')
                return redirect(url_for('crud_producto'))
            else:
                print(codiprod)
                crud_prod.insert_producto(datos)
                flash('Registro Creado ...!')
                return redirect(url_for('crud_producto'))

        elif accion=='act':
            print('UPDATE')
            datos = request.form
            print(datos)
            crud_prod.update_producto(request.form)
            flash('Registro Actualizado ...!')
            return redirect(url_for('crud_producto'))
            # return datos
        elif accion=='eli':
            print('DELETE')
            datos = request.form
            print(datos)
            crud_prod.delete_producto(request.form)
            flash('Registro Eliminado ...!')
            return redirect(url_for('crud_producto'))
            # return datos


@app.route('/producto', methods=["GET", "POST"])
def producto():
    modo = request.args.get('modo',None)
    id = request.args.get('id',None)
    form = frm_producto()
    #datos = crud_prod.get_productos()
    accion = request.form.get('accion',None)
    print(request.method)
    print('HOLA PRODUCTO')

    if id and id != None:
        dato  = crud_prod.sel_producto(id)

    if request.method == "GET":
        try:
            # aca se valida la existencia de la variable dato
            # esta es la manera correcta de validar la existencia de una variable en python
            dato
            data_existe = True
        except:
            data_existe = False

        if data_existe and dato != None:
            return render_template('producto.html', form=form, prod=dato, modo=modo)
        else:
            return render_template('producto.html', form=form, modo=modo)

    elif request.method == "POST":
        if form.validate_on_submit() and accion == 'ins':
            print('INSERT')
            datos = request.form
            print(datos)
            crud_prod.insert_producto(datos)
            flash('Registro Creado ...!')
            return redirect(url_for('lista_prod'))

        elif form.validate_on_submit() and accion=='act':
            print('UPDATE')
            datos = request.form
            print(datos)
            crud_prod.update_producto(request.form)
            flash('Registro Actualizado ...!')
            return redirect(url_for('lista_prod'))

        else:
            flash(form.errors)
            #print(form.errors)
            #return render_template('producto.html', form=form, prod=dato)
            return 'HOLA es el POST del formulario'
    #         # return render_template('producto.html', form=form, prod=dato)


@app.route('/eliminar/<string:id>')
def eliminar(id):
    # return 'HOLA ELIMINAR'
    # return render_template('eliminar.html')
    crud_prod.delete_producto(id)
    flash('Registro Eliminado ...!')
    return redirect(url_for('crear'))

@app.route('/editar')
def editar():
    return render_template('editar.html')

@app.route('/servicios')
def servicios():
    # return render_template('editar.html')
    return 'HOLA SERVICIOS'

@app.route('/contacto')
def contacto():
    # return render_template('editar.html')
    return 'HOLA CONTACTOS'

@app.route('/lista_producto')
def lista_prod():
    #return 'HOLA lista_productos'
        datos = crud_prod.get_productos()
        if datos and datos != None:
            return render_template('listado_productos.html', productos=datos)
        else:
            flash('No hay productos REGISTRADOS ...!')
            return redirect(url_for('home'))
            #return render_template('listado_productos.html', productos=datos)
            #return render_template('listado_productos.html', productos=crud_prod.get_productos())

if __name__ == "__main__":
    app.run(debug=True)