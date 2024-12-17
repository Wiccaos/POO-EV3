import Servicios.ConsumirAPI, Datos.jsonplace_db
import Modelos.User, Modelos.Address, Modelos.Company, Modelos.Post, Modelos.Todo

# Procesa los datos de las Tareas
def neg_todos():
    try:
        todo_id = int(input("Ingrese el ID de la tarea a consultar: "))
        todo = Servicios.ConsumirAPI.view_todos(todo_id)
        if todo:
            # Crear objeto Todo
            todo_obj = Modelos.Todo.Todo(
                userId=todo.userId,
                Id=todo.Id,
                title=todo.title,
                completed=todo.completed
            )
            print(f"\nUser ID: {todo_obj.userId}\nId de la Tarea: {todo_obj.Id}\nTítulo: {todo_obj.title}\nCompletada: {todo_obj.completed}")
            while True:
                answer = input("\n¿Desea Guardar la Tarea en la Base de Datos? (si/no): ")
                if answer == 'si':
                    Datos.jsonplace_db.save_todo_DB(todo_obj.Id, todo_obj.title, todo_obj.completed)
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
            # Crear objeto User
            user_obj = Modelos.User.User(
                userId=user.userId,
                name=user.name,
                username=user.username,
                email=user.email,
                website=user.website,
                phone=user.phone
            )
            # Crear objeto Company
            company_obj = Modelos.Company.Company(
                name_company=user_company.name_company,
                catch_phrase=user_company.catch_phrase,
                bs=user_company.bs,
                userId=user.userId
            )
            # Crear objeto Address
            address_obj = Modelos.Address.Address(
                street=user_address.street,
                suite=user_address.suite,
                city=user_address.city,
                zip_code=user_address.zip_code,
                lat=user_address.lat,
                lng=user_address.lng,
                userId=user.userId
            )

            print(f"\nUser ID: {user_obj.userId}\nNombre de Usuario: {user_obj.username}\nNombre: {user_obj.name}\nEmail: {user_obj.email}\nTeléfono: {user_obj.phone}\nSitio Web: {user_obj.website}")
            print(f"Compañía: {company_obj.name_company}\nDirección: {address_obj.suite}, {address_obj.street}, {address_obj.city}")
            while True:
                answer = input("\n¿Desea Guardar el Usuario en la Base de Datos? (si/no): ")
                if answer == 'si':
                    Datos.jsonplace_db.save_user_DB(
                        user_obj.userId,
                        user_obj.name,
                        user_obj.username,
                        user_obj.email,
                        user_obj.website,
                        user_obj.phone,
                        company_obj.name_company,
                        company_obj.catch_phrase,
                        company_obj.bs,
                        address_obj.street,
                        address_obj.suite,
                        address_obj.city,
                        address_obj.zip_code,
                        address_obj.lat,
                        address_obj.lng
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
        if post:
            # Crear objeto Post
            post_obj = Modelos.Post.Post(
                userId=post.userId,
                id=post.id,
                title=post.title,
                body=post.body
            )
            print(f"\nPost ID: {post_obj.id}\nUser ID: {post_obj.userId}\nTítulo: {post_obj.title}\nCuerpo: {post_obj.body}")
            while True:
                answer = input("\n¿Desea Guardar el post en la Base de Datos? (si/no): ")
                if answer == 'si':
                    Datos.jsonplace_db.save_post_DB(post_obj.id, post_obj.title, post_obj.body)
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