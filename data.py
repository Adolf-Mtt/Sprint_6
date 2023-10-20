# #Este documento .py contiene los datos(parámetros) en diccionarios para solicitudes

headers = {
    "Content-Type": "application/json"
}

# Parámetro en solicitud "post-> headers=" para crear un usuario
kit_headrers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "
}

# Parámetro en solicitud "post-> json=" para crear un usuario
user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

# Parámetro en solicitud "post-> json=" para crear un Kit
kit_body = {
    "name": "input_a_new_kit_name"
}
