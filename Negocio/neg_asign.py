import Datos.db_conection

def asign_post():
    try: 
        id_post = int(input("Ingrese el ID del post que desea asignar: "))
        userId = int(input("Ingrese el ID del usuario a asignar: "))
        Datos.db_conection.asign_post(id_post, userId)
    except ValueError:
        print("Error: Ambos IDs deben ser números enteros.")

def asign_todo():
    try:
        id_todo = int(input("Ingrese el ID de la tarea que desea asignar: "))
        userId = int(input("Ingrese el ID del usuario a asignar: "))
        Datos.db_conection.asign_todo(userId, id_todo)
    except ValueError:
        print("Error: Ambos IDs deben ser números enteros.")

