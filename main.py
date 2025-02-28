import json
from api.api import fetch_covid_data  # Asegúrate de que esta importación es correcta

def main():
    nombre_departamento = input("Ingrese el nombre del departamento: ")
    limite_registros = int(input("Ingrese el número de registros a consultar: "))

    resultados = fetch_covid_data(nombre_departamento, limite_registros)

    if resultados:
        print(json.dumps(resultados, indent=4, ensure_ascii=False))
    else:
        print("⚠️ No se encontraron datos.")

if __name__ == "__main__":
    main()  # Esto ejecuta la función cuando corres el script
