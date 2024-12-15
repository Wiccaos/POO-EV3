import Negocio.neg_jsonplaceholder, Negocio.neg_asign, Negocio.gestor_contrasenas
import Datos.db_conection
# from Servicios.serperApi import menu_serper
from Negocio.requests_serper import menu_serper

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

def menu_db():
    """Menú interacctivo para utilizar las funciones de la DB"""
    while True:
        print("""
Menú de la Base de Datos:
1. Mostrar Usuarios
2. Mostrar Posts
3. Mostrar Tareas
4. Asignar Post a un Usuario
5. Asignar Tarea a un Usuario
6. Desencriptar Contraseña
0. Salir de este menú
""")
        try:
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número")
            continue

        # Ver Users
        if option == 1:
            Datos.db_conection.view_user_DB()
        # Ver Posts
        if option == 2:
            Datos.db_conection.view_post_DB()
        # Ver Tareas
        if option == 3:
            Datos.db_conection.view_todo_DB()
        # Asignar Post
        if option == 4:
            Negocio.neg_asign.asign_post()
        # Asignar Tarea
        if option == 5:
            Negocio.neg_asign.asign_todo()
        if option == 6:
            user_id = input("Ingrese el ID del usuario para desencriptar: ")
            Datos.db_conection.decrypt_password_from_db(user_id)
        # Salir
        if option == 0:
            print("Volviendo al Menú principal...")
            break

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
            menu_serper()
        elif option == 0:
            print("Saliendo del programa...")
            break