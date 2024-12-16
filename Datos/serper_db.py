import Datos.db_conection
from prettytable import from_db_cursor

# Guarda la busqueda con serper en la DB
def save_busqueda(query):
    """Guarda la búsqueda en la base de datos y devuelve el ID de la búsqueda."""
    cnx = Datos.db_conection.conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query_sql = "INSERT INTO Busqueda (keyword_search) VALUES (%s);"
        cursor.execute(query_sql, (query,))
        cnx.commit()
        busqueda_id = cursor.lastrowid
        cursor.close()
        return busqueda_id

# Guarda el resultado de la busqueda en la DB
def save_resultado(busqueda_id, titulo, url, descripcion):
    """Guarda un resultado de búsqueda en la base de datos."""
    cnx = Datos.db_conection.conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query_sql = "INSERT INTO Resultados (Busqueda_id_search, titulo, url, descripcion) VALUES (%s, %s, %s, %s);"
        cursor.execute(query_sql, (busqueda_id, titulo, url, descripcion))
        cnx.commit()
        cursor.close()

def view_search_DB():
    """Muestra los resultados de la búsqueda en el terminal"""
    cnx = Datos.db_conection.conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = """
                    SELECT 
                        b.keyword_search as Busqueda,
                        r.titulo,
                        r.url,
                        r.descripcion
                    FROM 
                        Busqueda b
                    JOIN 
                        Resultados r ON b.id_search = r.Busqueda_id_search;"""
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay ToDos registrados en la DB\n")