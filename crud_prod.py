import sqlite3

# conn = sqlite3.connect("database/inventario.sqlite3") 
# con esta instruccion se crea la base de datos, si no existe
# y si existe se conecta a ella, pero no es necesario crearla aqui

conn = sqlite3.connect("data/IV.sqlite3", check_same_thread=False)
cursor = conn.cursor()

def close_conn():
    conn.close()

def get_productos():
    cursor.execute( '''
                    SELECT * FROM productos 
                    ORDER BY id DESC
                    ''')
    # return cursor.fetchall() de esta forma, o como sigue
    datos = cursor.fetchall() 
    return datos

def sel_producto(id):
    cursor.execute(f"SELECT * FROM productos WHERE id = '{id}'")
    datos = cursor.fetchone() 
    return datos

def get_producto(id):
    '''
    --- >
    cursor.execute( 'SELECT * FROM productos WHERE id = ?', id)
    no funcionó
    por que cuando el id paso a tener dos caracteres 
    lo estaba viendo como dos caracteres precisamente
    --- ///
    '''
    cursor.execute('''
                   SELECT * FROM productos WHERE id = {0} 
                   '''.format(id) )
    
    '''
    --- >
      SE PUEDE HACER DE FORMA COMO ESTA ARRIBA
      O DE ESTA OTRA FORMA

    # cursor.execute(f"SELECT * FROM productos WHERE id = '{id}'")

      ESTO DE AQUI USA f DE FORMAT, PARA CONSTRUIR CADENAS DE 
      TEXTO QUE TENGAN VALORES DINAMICOS, REFERENCIANDO EL VALOR QUE
      ESTA DENTRO DE LAS LLAVES {}
    ---- ///
    ''' 

    datos = cursor.fetchone() 
    return datos

def insert_producto(datos):
    cursor.execute('''
                   INSERT INTO productos
                   (codiprod, descprod, precprod, cantstoc)
                   VALUES
                   (?, ?, ?, ?)
                   ''', (datos["codiprod"], datos["descprod"], datos["precprod"], datos["cantstoc"],)
                   )
    conn.commit()
    conn.close   

def update_producto(data):
    cursor.execute('''
                   UPDATE productos 
                   SET descprod = ?, precprod = ?, cantstoc = ?
                   WHERE id = ?
                   ''' 
                   , 
                   (data["descprod"], data["precprod"], data["cantstoc"], data["id"],)
                   )
    conn.commit()
    conn.close   

def del_producto(id):
    cursor.execute('''
                   DELETE FROM productos 
                   WHERE id = {0} '''.format(id)
                   )
    conn.commit()
    conn.close   

def delete_producto(data):
    cursor.execute(''' DELETE FROM productos WHERE id = ? ''', (data["id"],) )
    conn.commit()
    conn.close   
