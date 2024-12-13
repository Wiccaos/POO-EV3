import mysql.connector
from prettytable import from_db_cursor
from Auxiliares.Constantes import db_user, db_password, db_host, db_database

# Conexion a DB
def conexion_db():
    try:
        cnx = mysql.connector.connect(
            user = db_user,
            password = db_password,
            host = db_host,
            database = db_database)
        return cnx
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None

# Guarda el usuario en la DB
def save_user_DB(userId, name, username, email, phone):
    """Guarda al usuario obtenido en jsonplaceholder en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "INSERT INTO User (id_user, username, user_email, user_website, user_phone) VALUES (%s,%s,%s,%s,%s);"
        cursor.execute(query, (userId, name, username, email, phone))
        cnx.commit()
        cursor.close()
    print("\nUsuario Guardado en la DB correctamente\n")

# Guarda el Post en la DB
def save_post_DB(id_post, post_title, body_post):
    """Guarda el post obtenido por jsonplaceholder en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "INSERT INTO Post (id_post, post_title, body_post) VALUES (%s, %s, %s);"
        cursor.execute(query, (id_post, post_title, body_post))
        cnx.commit()
        cursor.close()
        print("\nPost Guardado en la DB correctamente\n")

# Asigna un post a un usuario
def asign_post():
    """Asigna un Post a un usuario que se encuentre en la DB"""

    # Obtiene los datos para asignar
    id_post = int(input("Ingrese el ID del post que desea asignar: "))
    userId = int(input("Ingrese el ID del usuario a asignar: "))

    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "UPDATE Post SET User_id_user = %s WHERE id_post = %s;"
        cursor.execute(query, (id_post, userId))
        cnx.commit()
        cursor.close()
    print("\nEl post se ha asignado correctamente.\n")

# Guarda la Tarea en la DB
def save_todo(id_todo, todo_title, completed):
    """Guarda la Tarea desde Jsonplaceholder en la Base de Datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "INSERT INTO ToDos (id_todo, todo_title, completed) VALUES (%s, %s, %s);"
        cursor.execute(query, (id_todo, todo_title, completed))
        cnx.commit()
        cursor.close()
        print("\nTarea Guardada en la DB correctamente\n")

# Asigna una Tarea a un usuario
def asign_todo():
    """Función para asignar una tarea obtenida desde jsonplaceholder en la base de datos"""
    # Obtener datos
    id_todo = int(input("Ingrese el ID de la tarea que desea asignar: "))
    userId = int(input("Ingrese el ID del usuario a asignar: "))

    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "UPDATE ToDos SET User_id_user = %s WHERE id_todo = %s;"
        cursor.execute(query, (userId, id_todo))
        cnx.commit()
        cursor.close()
        print("\nLa tarea se ha asignado correctamente.\n")

# Ver Tabla de Usuarios
def view_user_DB():
    """Función para ver la tabla de usuarios en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT * FROM User;"
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay usuarios registrados en la DB\n")

# Ver tabla de Posts
def view_post_DB():
    """Función para ver la tabla de posts en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT * FROM Post;"
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay posts registrados en la DB\n")

# Ver tabla de ToDos
def view_todo_DB():
    """Función para ver la tabla de ToDos en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT * FROM ToDos;"
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay ToDos registrados en la DB\n")