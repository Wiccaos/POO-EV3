import Servicios.ConsumirAPI, DAL.db_conection

# Menú del sistema
def menu():
    """Menú interactivo para utilizar las funciones"""
    while True:
        print(""" 
Menú de JSONplaceholder
1. Consultar Datos de Usuario
2. Consultar Post
3. Salir
""")
        try: 
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número")
            continue  # Volver al inicio del bucle
              
        # User
        if option == 1:
            user = Servicios.ConsumirAPI.consultar_usuario()
            if user:
                answer = input("¿Desea Guardar el Usuario en la Base de Datos? (si/no): \n")
                if answer == 'si':
                    DAL.db_conection.save_user_DB(user.userId, user.name, user.username, user.email, user.phone)

        # Post
        elif option == 2:
            post = Servicios.ConsumirAPI.leer_post_por_id()
            if post:
                answer = input("¿Desea Guardar el post en la Base de Datos? (si/no): \n")
                if answer == 'si':
                    DAL.db_conection.save_post_DB(post.id, post.title, post.body)
                elif answer == 'no':
                    continue

        #Salir
        elif option == 3:
            print("Saliendo del programa...")
            break

menu()