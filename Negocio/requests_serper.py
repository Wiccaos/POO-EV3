import requests
import json
import Auxiliares.Constantes

url = Auxiliares.Constantes.SERPER_URL
def menu_serper():
    # Solicitar al usuario que ingrese la query
    query = input("Ingrese la query de búsqueda: ")

    payload = json.dumps({
        "q": query  # Usar la query ingresada por el usuario
    })
    headers = {
        'X-API-KEY': Auxiliares.Constantes.SERPER_API_KEY, # Esto tiene que cambiarlo el profe.
        'Content-Type': 'application/json'
    }

    response = requests.post(Auxiliares.Constantes.SERPER_URL, headers=headers, data=payload)

    if response.status_code == 200:
        results = response.json()
        print("Resultados de la búsqueda:")
        for result in results.get('organic', []):
            print(f"Título: {result['title']}")
            print(f"URL: {result['link']}")
            print(f"Descripción: {result['snippet']}\n")
    else:
        print(f"Error: {response.status_code} - {response.text}")