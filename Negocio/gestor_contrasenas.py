from cryptography.fernet import Fernet
import Datos.db_conection

# Generar una clave para la encriptación
def generate_key():
    return Fernet.generate_key()

# Encriptar la contraseña
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Desencriptar la contraseña
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def password_management():
    # Solicitar la contraseña al usuario
    password = input("Ingrese la contraseña que desea encriptar: ")
    print(f"Contraseña ingresada: {password}")

    # Generar una clave
    key = generate_key()
    print(f"Clave de encriptación generada: {key.decode()}")
    
    # Encriptar la contraseña
    encrypted_password = encrypt_password(password, key)
    print(f"Contraseña encriptada: {encrypted_password.decode()}")

    # Desencriptar la contraseña
    decrypted_password = decrypt_password(encrypted_password, key)
    print(f"Contraseña desencriptada: {decrypted_password}")

    # Comparar la contraseña original con la desencriptada
    if password == decrypted_password:
        print("La contraseña desencriptada coincide con la original.")
        
        # Solicitar el ID del usuario para guardar la contraseña.
        user_id = input("Ingrese el ID del usuario: ")
        
        #Guardar la contraseña encriptada.
        Datos.db_conection.save_encrypted_password(user_id, encrypted_password.decode(), key.decode())
    else:
        print("La contraseña desencriptada NO coincide con la original.")