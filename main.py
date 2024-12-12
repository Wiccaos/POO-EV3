import Servicios.ConsumirAPI, DAL.db_conection

# Menú del sistema
def menu():
    """Menú interactivo para utilizar las funciones"""
    while True:
        print(""" 
Menú de JSONplaceholder
1. Consultar Datos de Usuario
2. Consultar Post
3. Asignar Post a Usuario
4. Ver Tarea
9. Menú de la Base de datos
0. Salir
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

        # Asignar post
        elif option == 3:
            DAL.db_conection.asign_post()

        #Salir
        elif option == 0:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    menu()