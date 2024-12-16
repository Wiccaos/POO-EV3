import requests
import json
import Auxiliares.Constantes
import Datos.db_conection  # Asegúrate de importar tu módulo de conexión a la base de datos

def use_serper(query):
    payload = json.dumps({
        "q": query  # Usar la query ingresada por el usuario
    })
    headers = {
        'X-API-KEY': Auxiliares.Constantes.SERPER_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.post(Auxiliares.Constantes.SERPER_URL, headers=headers, data=payload)

    if response.status_code == 200:
        results = response.json()
        print("Resultados de la búsqueda:")
        
        # Guardar la búsqueda en la base de datos
        busqueda_id = Datos.db_conection.save_busqueda(query)  # Implementa esta función en tu módulo de conexión

        for result in results.get('organic', []):
            print(f"Título: {result['title']}")
            print(f"URL: {result['link']}")
            print(f"Descripción: {result['snippet']}\n")
            
            # Guardar cada resultado en la base de datos
            Datos.db_conection.save_resultado(busqueda_id, result['title'], result['link'], result['snippet'])  # Implementa esta función en tu módulo de conexión
    else:
        print(f"Error: {response.status_code} - {response.text}")