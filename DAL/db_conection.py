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
    
# Guarda el Post obtenido en la DB
def save_post_DB(id_post, post_title, body_post):
    """Función para guardar el post obtenido por jsonplaceholder en la DB"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "INSERT INTO Post (id_post, post_title, body_post) VALUES (%s, %s, %s);"
        cursor.execute(query, (id_post, post_title, body_post))
        cnx.commit()
        cursor.close()

# Guarda el usuario en la DB
def save_user_DB(userId, name, username, email, phone):
    """Función para guardar al usuario obtenido en JSON Placeholder en la DB"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "INSERT INTO User (id_user, username, user_email, user_website, user_phone) VALUES (%s,%s,%s,%s,%s);"
        cursor.execute(query, (userId, name, username, email, phone))
        cnx.commit()
        cursor.close()