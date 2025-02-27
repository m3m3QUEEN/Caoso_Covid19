# ui_module.py
def get_user_input():
    nombre_departamento = input("Ingrese el nombre del departamento: ")
    limite_registros = int(input("Ingrese el número de registros a consultar: "))
    return nombre_departamento, limite_registros

def display_results(results_df):
    print("\nResultados de la consulta:")
    print(results_df.to_string(index=False))