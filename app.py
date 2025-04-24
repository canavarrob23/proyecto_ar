from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import crud_prod

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
            #crud_prod.insert_producto(request.form) 
            crud_prod.insert_producto(datos) 
            flash('Registro Creado ...!')
            return redirect(url_for('crud_producto'))
            # return datos
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


@app.route('/eliminar/<string:id>')
def eliminar(id):
    # return 'HOLA ELIMINAR'
    # return render_template('eliminar.html')
    crud_prod.delete_producto(id)
    flash('Registro Eliminado ...!')
    return redirect(url_for('crear'))

@app.route('/editar')
def editar():
    return 'HOLA EDITAR'
    #return render_template('editar.html')

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
    return 'HOLA lista_productos'
    #return render_template('lista_productos.html')

if __name__ == "__main__":
    app.run(debug=True)