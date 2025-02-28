from sodapy import Socrata

# Conexión a la API
client = Socrata("www.datos.gov.co", None)

# Obtener datos (5 registros)
data = client.get("gt2j-8ykr", limit=5)

# Imprimir datos
print(data)
