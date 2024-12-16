import mysql.connector
from prettytable import from_db_cursor
from Auxiliares.Constantes import db_user, db_password, db_host, db_database
from Negocio.gestor_contrasenas import decrypt_password

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
def save_user_DB(userId, name, username, email, user_website, phone, company_name, company_catch_phrase, company_bs, address_street, address_suite, address_city, address_zipcode, address_lat, address_lng):
    """Guarda al usuario obtenido en jsonplaceholder en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        try:
            # Inserta el usuario en la db
            query = "INSERT INTO User (id_user, name, username, user_email, user_website, user_phone) VALUES (%s,%s,%s,%s,%s,%s);"
            cursor.execute(query, (userId, name, username, email, user_website, phone))
            cnx.commit()

            # Inserta la compañía en la db
            query_company = """
                INSERT INTO Companies (User_id_user, name_company, catchPhrase, bs) 
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query_company, (userId, company_name, company_catch_phrase, company_bs))
            
            # Inserta la dirección en la db
            query_address = """
                INSERT INTO Address (User_id_user, street, suite, city, zip_code, lat, lng) 
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query_address, (userId, address_street, address_suite, address_city, address_zipcode, address_lat, address_lng))
            
            cnx.commit()
            print("\nUsuario, compañía y dirección guardados en la DB correctamente\n")
        except mysql.connector.IntegrityError as err:
            print(f"Error de integridad: {err} - Puede que ya exista un usuario con el mismo ID.")
        except mysql.connector.Error as err:
            print(f"Error al guardar el usuario: {err}")
        finally:
            cursor.close()
    else:
        print("No se pudo establecer conexión con la base de datos.")

# Guarda el Post en la DB
def save_post_DB(id_post, post_title, body_post):
    """Guarda el post obtenido por jsonplaceholder en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        try:
            query = "INSERT INTO Post (id_post, post_title, body_post) VALUES (%s, %s, %s);"
            cursor.execute(query, (id_post, post_title, body_post))
            cnx.commit()
            print("\nPost Guardado en la DB correctamente\n")
        except mysql.connector.IntegrityError as err:
            print(f"Error de integridad: {err} - Puede que ya exista un post con el mismo ID.")
        except mysql.connector.Error as err:
            print(f"Error al guardar el post: {err}")
        finally:
            cursor.close()

# Asigna un post a un usuario
def asign_post(id_post, userId):
    """Asigna un Post a un usuario que se encuentre en la DB"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "UPDATE Post SET User_id_user = %s WHERE id_post = %s;"
        cursor.execute(query, (userId, id_post))
        cnx.commit()
        cursor.close()
    print("\nEl post se ha asignado correctamente.\n")

# Guarda la Tarea en la DB
def save_todo(id_todo, todo_title, completed):
    """Guarda la Tarea desde Jsonplaceholder en la Base de Datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        try:
            query = "INSERT INTO ToDos (id_todo, todo_title, completed) VALUES (%s, %s, %s);"
            cursor.execute(query, (id_todo, todo_title, completed))
            cnx.commit()
            print("\nTarea Guardada en la DB correctamente\n")
        except mysql.connector.IntegrityError as err:
            print(f"Error de integridad: {err} - Puede que ya exista una tarea con el mismo ID.")
        except mysql.connector.Error as err:
            print(f"Error al guardar la tarea: {err}")
        finally:
            cursor.close()

# Asigna una Tarea a un usuario
def asign_todo(userId,id_todo):
    """Función para asignar una tarea obtenida desde jsonplaceholder en la base de datos"""
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
    """Función para ver la tabla de usuarios en la base de datos junto con su dirección y compañía"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = """
                SELECT 
                    u.id_user AS 'ID',
                    u.name AS 'Nombre',
                    u.username AS 'Nombre de Usuario',
                    u.user_email AS 'Email',
                    u.user_phone AS 'Teléfono',
                    u.user_website AS 'Sitio Web',
                    CONCAT_WS(', ', a.suite, a.street, a.city) AS 'Dirección', 
                    c.name_company AS 'Compañía'
                FROM 
                    User u
                LEFT JOIN 
                    Address a ON u.id_user = a.User_id_user
                LEFT JOIN 
                    Companies c ON u.id_user = c.User_id_user;
        """
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay usuarios registrados en la DB\n")
        finally:
            cursor.close()
    else:
        print("No se pudo establecer conexión con la base de datos.")

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

# Guardar contraseña encriptada.
def save_encrypted_password(user_id, encrypted_password, encryption_key):
    """Guarda la contraseña encriptada en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        # Verificar si el user_id existe
        cursor.execute("SELECT id_user FROM User WHERE id_user = %s;", (user_id,))
        if cursor.fetchone() is None:
            print("\nEl usuario ingresado no existe en la DB. No se puede guardar la contraseña.")
            cursor.close()
            return  # Salir de la función si el usuario no existe

        # Si el usuario existe, proceder a guardar la contraseña
        query = "INSERT INTO UserPasswords (user_id, encrypted_password, encryption_key) VALUES (%s, %s, %s);"
        cursor.execute(query, (user_id, encrypted_password, encryption_key))
        cnx.commit()
        cursor.close()
        print("\nContraseña encriptada guardada en la DB correctamente\n")

# Desencriptar contraseña
def get_encrypted_password(user_id):
    """Recupera la contraseña encriptada y la clave de encriptación de la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT encrypted_password, encryption_key FROM UserPasswords WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result  # Devuelve una tupla (encrypted_password, encryption_key)
        else:
            print("No se encontró la contraseña para el usuario especificado.")
            return None

# Desencripta la constraseña desde la db
def decrypt_password_from_db(user_id):
    """Desencripta la contraseña almacenada en la base de datos y la muestra en el terminal"""
    data = get_encrypted_password(user_id)
    if data:
        encrypted_password, encryption_key = data
        decrypted_password = decrypt_password(encrypted_password.encode(), encryption_key.encode())
        print(f"La contraseña desencriptada para el usuario {user_id} es: {decrypted_password}")

# Guarda la busqueda con serper en la DB
def save_busqueda(query):
    """Guarda la búsqueda en la base de datos y devuelve el ID de la búsqueda."""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query_sql = "INSERT INTO Busqueda (keyword_search) VALUES (%s);"
        cursor.execute(query_sql, (query,))
        cnx.commit()
        busqueda_id = cursor.lastrowid  # Obtiene el ID de la última inserción
        cursor.close()
        return busqueda_id

# Guarda el resultado de la busqueda en la DB
def save_resultado(busqueda_id, titulo, url, descripcion):
    """Guarda un resultado de búsqueda en la base de datos."""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query_sql = "INSERT INTO Resultados (Busqueda_id_search, titulo, url, descripcion) VALUES (%s, %s, %s, %s);"
        cursor.execute(query_sql, (busqueda_id, titulo, url, descripcion))
        cnx.commit()
        cursor.close()

def view_search_DB():
    """Muestra los resultados de la búsqueda en el terminal"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = """
                    SELECT 
                        b.keyword_search as Busqueda,
                        r.titulo,
                        r.url,
                        r.descripcion
                    FROM 
                        Busqueda b
                    JOIN 
                        Resultados r ON b.id_search = r.Busqueda_id_search;"""
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay ToDos registrados en la DB\n")

