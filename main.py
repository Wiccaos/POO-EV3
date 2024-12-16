import Datos.encrypt_db
import Datos.jsonplace_db
import Datos.serper_db
import Negocio.neg_jsonplaceholder, Negocio.neg_asign, Negocio.gestor_contrasenas, Negocio.neg_serper
import Datos.db_conection

# Menú de jsonplaceholder
def menu_json():
    """Menú interactivo para utilizar las funciones en jsonplaceholder"""
    while True:
        print(""" 
Menú de JsonPlaceholder:
1. Consultar Datos de Usuario
2. Consultar Post
3. Consultar Tarea
0. Salir de este menú
""")
        try: 
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número")
            continue  # Volver al inicio del bucle
        # User
        if option == 1:
            Negocio.neg_jsonplaceholder.neg_user()
        # Post
        elif option == 2:
            Negocio.neg_jsonplaceholder.neg_post()
        # Tarea
        elif option == 3:
            Negocio.neg_jsonplaceholder.neg_todos()
        #Salir
        elif option == 0:
            print("Volviendo al menú principal...")
            break
        else:
            print("Error: Opción no válida. Por favor, vuelva a intentarlo.")

def menu_db():
    """Menú interacctivo para utilizar las funciones de la DB"""
    while True:
        print("""
Menú de la Base de Datos:
1. Mostrar Usuarios
2. Mostrar Posts
3. Mostrar Tareas
4. Mostrar Busquedas y Resultados
5. Asignar Post a un Usuario
6. Asignar Tarea a un Usuario
7. Desencriptar Contraseña
0. Salir de este menú
""")
        try:
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número")
            continue

        # Ver Users
        if option == 1:
            Datos.jsonplace_db.view_user_DB()
        # Ver Posts
        elif option == 2:
            Datos.jsonplace_db.view_post_DB()
        # Ver Tareas
        elif option == 3:
            Datos.jsonplace_db.view_todo_DB()
        # Ver Busquedas y Resultados
        elif option == 4:
            Datos.serper_db.view_search_DB()
        # Asignar Post
        elif option == 5:
            Negocio.neg_jsonplaceholder.asign_post()
        # Asignar Tarea
        elif option == 6:
            Negocio.neg_jsonplaceholder.asign_todo()
        elif option == 7:
            user_id = input("Ingrese el ID del usuario para desencriptar: ")
            Negocio.gestor_contrasenas.decrypt_password_from_db(user_id)
        # Salir
        elif option == 0:
            print("Volviendo al Menú principal...")
            break
        else:
            print("Error: Opción no válida. Por favor, vuelva a intentarlo.")

# Menú para ejecutar el programa
if __name__ == "__main__":
    while True:
        print("""
Menú del Programa:
1. Menú de JsonPlaceholder.
2. Menú de la Base de Datos.
3. Menú de encriptación.
4. Menú de Serper.
0. Salir""")
        option = int(input("Ingrese una opción: "))
        if option == 1:
            menu_json()
        elif option == 2:
            menu_db()
        elif option == 3:
            Negocio.gestor_contrasenas.password_management()
        elif option == 4:
            Negocio.neg_serper.manage_serper()
        elif option == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Error: Opción no válida. Por favor, vuelva a intentarlo.")
