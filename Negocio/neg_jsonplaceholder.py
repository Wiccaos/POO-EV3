import Servicios.ConsumirAPI, Datos.jsonplace_db

# Procesa los datos de las Tareas
def neg_todos():
    try:
        todo_id = int(input("Ingrese el ID de la tarea a consultar: "))
        todo = Servicios.ConsumirAPI.view_todos(todo_id)
        if todo:  # Verifica si 'todos' fue correctamente inicializado
            print(f"\nUser  ID: {todo.userId}\nId de la Tarea: {todo.Id}\nTítulo de la tarea: {todo.title}\nEstado de la tarea: {todo.completed}")
            while True:
                answer = input("\n¿Desea Guardar la Tarea en la Base de Datos? (si/no): ")
                if answer == 'si':
                    Datos.jsonplace_db.save_todo(todo.Id, todo.title, todo.completed)
                    break
                elif answer == 'no':
                    print("\nLa Tarea NO se ha guardado en la DB\n")
                    break
                else:
                    print("Respuesta invalida")
        else:
            print("No se pudieron obtener los datos de la tarea.")
    except ValueError:
        print("Error: El ID ingresado no es un número entero.")

# Procesa los datos de los Usuarios
def neg_user():
    try:
        user_id = int(input("Ingrese el ID del usuario a consultar: "))
        user, user_company, user_address = Servicios.ConsumirAPI.view_user(user_id)
        if user:
            print(f"\nUser    ID: {user.userId}\nNombre de Usuario: {user.username}\nNombre: {user.name}\nEmail: {user.email}\nTeléfono: {user.phone}\nSitio Web: {user.website}")
            print(f"Compañía: {user_company.name_company}\nDirección: {user_address.suite}, {user_address.street}, {user_address.city}")
            while True:
                answer = input("\n¿Desea Guardar el Usuario en la Base de Datos? (si/no): ")
                if answer == 'si':
                    Datos.jsonplace_db.save_user_DB(
                        user.userId,
                        user.name,
                        user.username,
                        user.email,
                        user.website,
                        user.phone,
                        user_company.name_company,
                        user_company.catch_phrase,
                        user_company.bs,
                        user_address.street,
                        user_address.suite,
                        user_address.city,
                        user_address.zip_code,
                        user_address.lat,
                        user_address.lng
                    )
                    break
                elif answer == 'no':
                    print("\nEl Usuario NO se ha guardado en la DB\n")
                    break
                else:
                    print("Respuesta invalida")
        else:
            print("No se pudieron obtener los datos del usuario.")
    except ValueError:
        print("Error: El ID ingresado no es un número entero.")

# Procesa los datos de los Post
def neg_post():
    try:
        post_id = int(input("Ingrese el ID del post que desea leer: "))
        post = Servicios.ConsumirAPI.read_post(post_id)
        if post:  # Verifica si 'post' fue correctamente inicializado
            print(f"\nPost ID: {post.id}\nUserID: {post.userId}\nTítulo: {post.title}\nCuerpo: {post.body}")
            while True:
                answer = input("\n¿Desea Guardar el post en la Base de Datos? (si/no): ")
                if answer == 'si':
                    Datos.jsonplace_db.save_post_DB(post.id, post.title, post.body)
                    break
                elif answer == 'no':
                    print("\nEl Post NO se ha guardado en la DB\n")
                    break
                else:
                    print("Respuesta invalida")
        else:
            print("No se pudieron obtener los datos del post.")
    except ValueError:
        print("Error: El ID ingresado no es un número entero.")