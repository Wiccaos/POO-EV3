import requests
from Modelos import Post, Users, Todo, Companies, Address
import Auxiliares.Constantes 

# Mostrar post
def read_post(post_id):
    """Función para leer un post desde JSON Placeholder según el id"""
    try:
        ans = requests.get(f"{Auxiliares.Constantes.URL_Post}/{post_id}")
        ans.raise_for_status()  # Lanza un error si la respuesta no es 200
        post_data = ans.json()
        
        # Crear una instancia de Post y asignar los valores
        post = Post.Post()
        post.userId = post_data.get('userId')
        post.id = post_data.get('id')
        post.title = post_data.get('title')
        post.body = post_data.get('body')
        return post
    
    # Manejo de errores
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("El post no fue encontrado.")

# Ver usuario
def view_user(user_id):
    """Función para consultar los datos de usuario por el id"""
    try:
        ans = requests.get(f"{Auxiliares.Constantes.URL_Users}/{user_id}")
        ans.raise_for_status()  # Lanza un error si la respuesta no es 200
        user_data = ans.json()

        # Crear una instancia de Usuario y asignar los valores
        user = Users.User()
        user.userId = user_data.get('id')
        user.name = user_data.get('name')
        user.username = user_data.get('username')
        user.email = user_data.get('email')
        user.website = user_data.get('website')
        user.phone = user_data.get('phone')

        # Crear una instancia de Companies y asignar los valores
        user_company = Companies.Companies()
        user_company.name_company = user_data.get('company', {}).get('name')
        user_company.catch_phrase = user_data.get('company', {}).get('catchPhrase')
        user_company.bs = user_data.get('company', {}).get('bs')
        user_company.userId = user_data.get('id')

        # Crear una instancia de Address y asignar los valores
        user_address = Address.Address(
            street=user_data.get('address', {}).get('street'),
            suite=user_data.get('address', {}).get('suite'),
            city=user_data.get('address', {}).get('city'),
            zip_code=user_data.get('address', {}).get('zipcode'),
            lat=user_data.get('address', {}).get('geo', {}).get('lat'),
            lng=user_data.get('address', {}).get('geo', {}).get('lng'),
            userId=user_data.get('id')
        )
        
        return user, user_company, user_address
    

    # Manejo de errores
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("El usuario no fue encontrado.")

# Ver Lista de Tareas
def view_todos(todo_id):
    """Función para consultar los datos de las tareas por el id del usuario"""
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
    
    # Manejo de errores
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("El usuario no fue encontrado.")