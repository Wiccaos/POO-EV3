import Servicios.requests_serper

def manage_serper():
    # Solicitar al usuario que ingrese la query
    query = input("Ingrese la query de búsqueda: ")
    Servicios.requests_serper.use_serper(query)
