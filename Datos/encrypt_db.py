import Datos.db_conection

# Guardar contraseña encriptada.
def save_encrypted_password(user_id, encrypted_password, encryption_key):
    """Guarda la contraseña encriptada en la base de datos"""
    cnx = Datos.db_conection.conexion_db()
    if cnx:
        cursor = cnx.cursor()
        cursor.execute("SELECT id_user FROM User WHERE id_user = %s;", (user_id,))
        if cursor.fetchone() is None:
            print("\nEl usuario ingresado no existe en la DB. No se puede guardar la contraseña.")
            cursor.close()
            return

        # Si el usuario existe, proceder a guardar la contraseña
        query = "INSERT INTO UserPasswords (user_id, encrypted_password, encryption_key) VALUES (%s, %s, %s);"
        cursor.execute(query, (user_id, encrypted_password, encryption_key))
        cnx.commit()
        cursor.close()
        print("\nContraseña encriptada guardada en la DB correctamente\n")

# Desencriptar contraseña
def get_encrypted_password(user_id):
    """Recupera la contraseña encriptada y la clave de encriptación de la base de datos"""
    cnx = Datos.db_conection.conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT encrypted_password, encryption_key FROM UserPasswords WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result
        else:
            print("No se encontró la contraseña para el usuario especificado.")
            return None