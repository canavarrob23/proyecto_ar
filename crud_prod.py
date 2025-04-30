import sqlite3

# conn = sqlite3.connect("database/inventario.sqlite3") 
# con esta instruccion se crea la base de datos, si no existe
# y si existe se conecta a ella, pero no es necesario crearla aqui

DATABASE = "data/IV.sqlite3"
# CONEXION A LA BD
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# CERRAR CONEXION A LA BD
def close_db(conn):
    if conn:
        conn.close()

# OBTENER TODOS LOS PRODUCTOS    
def get_productos():
    conn= get_db()
    cursor = conn.cursor()  
    SQL='''SELECT * FROM productos  ORDER BY id DESC '''
    cursor.execute(SQL)

    # return cursor.fetchall() de esta forma, o como sigue
    datos = cursor.fetchall() 
    close_db(conn)
    # conn.close() # no es necesario cerrar la conexion aqui, ya que se cierra en la funcion close_conn     
    # porque se sugiere esto
    return datos

# OBTENER UN PRODUCTO POR ID
def sel_producto(id):
    conn= get_db()
    cursor = conn.cursor()  
    SQL='''SELECT * FROM productos WHERE id = {0} '''.format(id)
    #cursor.execute(f"SELECT * FROM productos WHERE id = '{id}'")
    cursor.execute(SQL)
    datos = cursor.fetchone() 
    close_db(conn)
    return datos

# OBTENER UN PRODUCTO POR CODIGO DE PRODUCTO
def get_producto(codiprod):
    '''
    --- >
    cursor.execute( 'SELECT * FROM productos WHERE id = ?', id)
    no funcionó
    por que cuando el id paso a tener dos caracteres 
    lo estaba viendo como dos caracteres precisamente
    --- ///
    '''
    conn = get_db()
    cursor = conn.cursor()
    prod = codiprod.upper() # convertir a minusculas  
    #SQL='''SELECT * FROM productos WHERE codiprod = {1} '''.format(codiprod)
    SQL='''SELECT * FROM productos WHERE codiprod = ? '''
    #cursor.execute(SQL.format(codiprod) )
    cursor.execute(SQL, (prod,) )
    datos = cursor.fetchone() 
    close_db(conn)
    
    '''
      SE PUEDE HACER DE FORMA COMO ESTA ARRIBA
      O DE ESTA OTRA FORMA

    # cursor.execute(f"SELECT * FROM productos WHERE id = '{id}'")

      ESTO DE AQUI USA f DE FORMAT, PARA CONSTRUIR CADENAS DE 
      TEXTO QUE TENGAN VALORES DINAMICOS, REFERENCIANDO EL VALOR QUE
      ESTA DENTRO DE LAS LLAVES {}
    ''' 
    #print('datos ', datos)
    return datos


def insert_producto(datos):
    conn= get_db()
    cursor = conn.cursor()
    #codiprod = datos["codiprod"].upper() 

    SQL='''INSERT INTO productos
        (codiprod, descprod, precprod, cantstoc)
        VALUES (?, ?, ?, ?)
        '''
    cursor.execute(SQL, (datos["codiprod"].upper(), datos["descprod"].upper() , datos["precprod"], datos["cantstoc"],) )
    conn.commit()
    close_db(conn)

    # try:
    #     if codiprod and codiprod != None:
    #         exist_prod  = get_producto(codiprod)

    #     if exist_prod:
    #         print('El producto ya existe')
    #         #return('El producto ya existe ...!')
    #         return False    
    #     else:
    #         SQL='''INSERT INTO productos
    #             (codiprod, descprod, precprod, cantstoc)
    #             VALUES (?, ?, ?, ?)
    #             '''
    #         cursor.execute(SQL, (datos["codiprod"].upper(), datos["descprod"].upper() , datos["precprod"], datos["cantstoc"],) )
    #         conn.commit()
    # finally:
    #     close_db(conn)   

def update_producto(data):
    conn= get_db()
    cursor = conn.cursor()  
    cursor.execute('''
                   UPDATE productos 
                   SET descprod = ?, precprod = ?, cantstoc = ?
                   WHERE id = ?
                   ''' 
                   , 
                   (data["descprod"], data["precprod"], data["cantstoc"], data["id"],)
                   )
    conn.commit()
    close_db(conn)

def del_producto(id):
    conn= get_db()
    cursor = conn.cursor()  
    cursor.execute('''
                   DELETE FROM productos 
                   WHERE id = {0} '''.format(id)
                   )
    conn.commit()
    #conn.close
    close_db(conn) # no es necesario cerrar la conexion aqui, ya que se cierra en la funcion close_conn

def delete_producto(data):
    conn= get_db()
    cursor = conn.cursor()  
    cursor.execute(''' DELETE FROM productos WHERE id = ? ''', (data["id"],) )
    conn.commit()
    #conn.close   
    close_db(conn) # no es necesario cerrar la conexion aqui, ya que se cierra en la funcion close_conn
