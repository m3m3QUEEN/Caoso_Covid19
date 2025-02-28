from sodapy import Socrata

def fetch_covid_data(nombre_departamento, limite_registros):
    BASE_URL = "www.datos.gov.co"
    DATASET_ID = "gt2j-8ykr"

    try:
        cliente = Socrata(BASE_URL, None)

        # Formato correcto para filtrar por departamento
        query = f"departamento_nom='{nombre_departamento.upper()}'"  # Mayúsculas por si acaso
        resultados = cliente.get(DATASET_ID, where=query, limit=limite_registros)

        if not resultados:
            print("⚠️ No se encontraron datos para el departamento ingresado. Revisa el nombre o intenta con otro.")
        
        return resultados
    except Exception as e:
        print(f"Error al obtener los datos: {e}")
        return []
