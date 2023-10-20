#Este documento .py contiene las funciones para generar solicitudes [get / post]

import requests
import configuration
import data

# Función para consultar tabla de usuarios y obtener el authToken del primer usuario
# ENDPOIND "/api/db/resources/user_model.csv"
def get_users_token():
    var = requests.get(configuration.URL_API_DOC + configuration.USERS_TABLE_PATH)
    split = var.text.rsplit("\n") # Separador de líneas
    lista = split[1].rsplit(",") # Del indice '1' de la tabla usuarios, crear una lista
    token = len(lista)-1 # Token es el último ítem de la lista
    return var, lista[token]


# Función para crear un usuario
# ENDPOIND "/api/v1/users"
def post_create_user():
    return requests.post(configuration.URL_API_DOC + configuration.CREATE_USER_PATH,
                         json=data.user_body, headers=data.headers)


# Función para crear un Kit
# ENDPOIND "/api/v1/users" -- Parámetros: "body" y "header"
def post_new_client_kit(kit_body):
    token = get_users_token()
    kit_headers = data.kit_headrers.copy()
    kit_headers["Authorization"] = "Bearer "+token[1]

    return requests.post(configuration.URL_API_DOC + configuration.CREATE_KIT_PATH,
                         json=kit_body, headers=kit_headers)


# Función para consultar la tabla Kit, usando el parámetro "Authorization"
# el cual devuelve todos los Kits de un usuario
# ENDPOIND "/api/v1/kits"
def get_kit_table():
    token = get_users_token()
    header = {"Authorization": "Bearer "+token[1] }

    return requests.get(configuration.URL_API_DOC + configuration.KIT_TABLE_PATH,
                        headers=header)
