import mysql.connector
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
def save_todo():
    """Guarda la Tarea desde Jsonplaceholder en la Base de Datos"""
    pass

# Asigna una Tarea a un usuario
def asign_todo():

    # Obtener datos
    id_todo = int(input(""))
    userId = int(input(""))

    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = ""
        cursor.execute(query, (id_todo, userId))
        cnx.commit()
        cursor.close()