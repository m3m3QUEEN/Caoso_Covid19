# main.py
from api import fetch_covid_data  # Importa desde api.py
from ui import get_user_input, display_results  # Importa desde ui.py

def main():
    nombre_departamento, limite_registros = get_user_input()
    results_df = fetch_covid_data(nombre_departamento, limite_registros)
    display_results(results_df)

if __name__ == "__main__":
    main()