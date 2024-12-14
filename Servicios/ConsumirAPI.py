import requests
from Modelos.Post import Post
from Modelos.Users import User
from Modelos.Todo import Todo
import Auxiliares.Constantes 

# Mostrar post
def read_post():
    """Función para leer un post desde JSON Placeholder según el id"""

    post_id = int(input("Ingrese el ID del post que desea leer: "))

    try:
        ans = requests.get(f"{Auxiliares.Constantes.URL_Post}/{post_id}")
        ans.raise_for_status()  # Lanza un error si la respuesta no es 200
        post_data = ans.json()
        
        # Crear una instancia de Post y asignar los valores
        post = Post()
        post.userId = post_data.get('userId')
        post.id = post_data.get('id')
        post.title = post_data.get('title')
        post.body = post_data.get('body')
        
        return post
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("El post no fue encontrado.")

    finally:
        print(f"\nPost ID: {post.id}\nUserID: {post.userId}\nTítulo: {post.title}\nCuerpo: {post.body}")

# Ver usuario
def view_user():
    """Función para consultar los datos de usuario por el id"""
    user_id = int(input("Ingrese el ID del usuario a consultar: "))
    user = None

    try:
        ans = requests.get(f"{Auxiliares.Constantes.URL_Users}/{user_id}")
        ans.raise_for_status()  # Lanza un error si la respuesta no es 200
        user_data = ans.json()

        # Crear una instancia de Usuario y asignar los valores
        user = User()
        user.userId = user_data.get('id')
        user.name = user_data.get('name')
        user.username = user_data.get('username')
        user.email = user_data.get('email')
        user.phone = user_data.get('phone')
        return user

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("El usuario no fue encontrado.")

    finally:
        if user:  # Verifica si `user` fue correctamente inicializado
            print(f"\nUser  ID: {user.userId}\nNombre de Usuario: {user.username}\nNombre: {user.name}\nEmail: {user.email}\nTeléfono: {user.phone}")
        else:
            print("No se pudieron obtener los datos del usuario.")

# Ver Lista de Tareas
def view_todos():
    """Función para consultar los datos de las tareas por el id del usuario"""
    todo_id = int(input("Ingrese el ID de la tarea a consultar: "))
    todo = None
    try:
        ans = requests.get(f"{Auxiliares.Constantes.URL_Todo}/{todo_id}")
        ans.raise_for_status()  # Lanza un error si la respuesta no es 200
        todos_data = ans.json()

        # Crear una instancia de "To Do's" y asignar valores
        todo = Todo()
        todo.userId = todos_data.get('userId')
        todo.Id = todos_data.get('id')
        todo.title = todos_data.get('title')
        todo.completed = todos_data.get('completed')
        return todo
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("El usuario no fue encontrado.")
    
    finally:
        if todo:  # Verifica si 'todos' fue correctamente inicializado
            print(f"\nUser  ID: {todo.userId}\nId de la Tarea: {todo.Id}\nTítulo de la tarea: {todo.title}\nEstado de la tarea: {todo.completed}")
        else:
            print("No se pudieron obtener los datos de la tarea.")

