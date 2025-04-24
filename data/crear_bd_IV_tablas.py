import sqlite3

# Define el nombre del archivo de la base de datos
database = 'IV.sqlite3'


def crear_tablas():
    try:
        # Intenta conectar a la base de datos. Si no existe, se creará.
        conn = sqlite3.connect(database)
        print(f"Base de datos '{database}' creada o conectada exitosamente.")
        cursor = conn.cursor()


        # Aquí puedes realizar operaciones en la base de datos (crear tablas, insertar datos, etc.)

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codiprod TEXT NOT NULL,
                    descprod TEXT NOT NULL,
                    precprod REAL NOT NULL,
                    cantstoc REAL NOT NULL)
                    ''')
        
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Error al conectar o crear la base de datos: {e}")
    finally:
        # Asegúrate de cerrar la conexión si está abierta
        if 'conn' in locals() and conn:
            conn.close()
            print("Conexión a la base de datos cerrada.")

if __name__ == '__main__':
    crear_tablas()