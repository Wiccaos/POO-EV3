import requests
import json
import Auxiliares.Constantes
import Datos.jsonplace_db
import Datos.serper_db

def use_serper(query):
    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': Auxiliares.Constantes.SERPER_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.post(Auxiliares.Constantes.SERPER_URL, headers=headers, data=payload)

    if response.status_code == 200:
        results = response.json()
        print("\nResultados de la búsqueda:")
        
        # Guarda la búsqueda en la base de datos
        busqueda_id = Datos.serper_db.save_busqueda(query)

        for result in results.get('organic', []):
            print(f"Título: {result['title']}")
            print(f"URL: {result['link']}")
            print(f"Descripción: {result['snippet']}\n")
            
            # Guarda cada resultado en la base de datos
            Datos.serper_db.save_resultado(busqueda_id, result['title'], result['link'], result['snippet'])
    else:
        print(f"Error: {response.status_code} - {response.text}")