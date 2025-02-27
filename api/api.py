# api_module.py
import pandas as pd
from sodapy import Socrata

def fetch_covid_data(nombre_departamento, limite_registros):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit=limite_registros, departamento=nombre_departamento)
    results_df = pd.DataFrame.from_records(results)
    
    # Filtrar las columnas requeridas
    filtered_df = results_df[['ciudad_de_ubicacion', 'departamento', 'edad', 'tipo', 'estado', 'pais_de_procedencia']]
    return filtered_df