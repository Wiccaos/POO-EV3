from DAL.db_conection import decrypt_password_from_db
import Servicios.ConsumirAPI, DAL.db_conection
import Servicios.gestor_contrasenas
from Servicios.gestor_contrasenas import password_management
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
            user = Servicios.ConsumirAPI.view_user()
            if user:
                answer = input("\n¿Desea Guardar el Usuario en la Base de Datos? (si/no): ")
                if answer == 'si':
                    DAL.db_conection.save_user_DB(user.userId, user.name, user.username, user.email, user.phone)
                elif answer == 'no':
                    print("\nEl Usuario no se ha guardado en la DB\n")
                    continue

        # Post
        elif option == 2:
            post = Servicios.ConsumirAPI.read_post()
            if post:
                answer = input("\n¿Desea Guardar el post en la Base de Datos? (si/no): ")
                if answer == 'si':
                    DAL.db_conection.save_post_DB(post.id, post.title, post.body)
                elif answer == 'no':
                    print("\nEl Post no se ha guardado en la DB\n")
                    continue

        # Tarea
        elif option == 3:
            todo = Servicios.ConsumirAPI.view_todos()
            if todo:
                answer = input("\n¿Desea Guardar la Tarea en la Base de Datos? (si/no): ")
                if answer == 'si':
                    DAL.db_conection.save_todo(todo.Id, todo.title, todo.completed)
                elif answer == 'no':
                    print("\nLa Tarea no se ha guardado en la DB\n")

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
            return

        # Ver Users
        if option == 1:
            DAL.db_conection.view_user_DB()
            continue
        # Ver Posts
        if option == 2:
            DAL.db_conection.view_post_DB()
            continue
        # Ver Tareas
        if option == 3:
            DAL.db_conection.view_todo_DB()
            continue
        # Asignar Post
        if option == 4:
            DAL.db_conection.asign_post()
            continue
        # Asignar Tarea
        if option == 5:
            DAL.db_conection.asign_todo()
            continue
        if option == 6:
            user_id = input("Ingrese el ID del usuario para desencriptar: ")
            decrypt_password_from_db(user_id)
            continue
        # Salir
        if option == 0:
            print("Volviendo al Menú principal...")
            break

# Ejecutar el programa
if __name__ == "__main__":
    while True:
        print("""
Menú del Programa:
1. Menú de JsonPlaceholder.
2. Menú de la Base de Datos.
3. Menú de Contraseñas. 
0. Salir""")
        option = int(input("Ingrese una opción: "))
        if option == 1:
            menu_json()
        elif option == 2:
            menu_db()
        elif option == 3:
            password_management()
        elif option == 0:
            print("Saliendo del programa...")
            break