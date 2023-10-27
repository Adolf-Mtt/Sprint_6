# Este documento .py contiene las funciones para generar los autotest
import sender_stand_request
import data

# Función para generar el nombre del KIT con parametro json
#
def get_kit_body(kit_name):
    name = data.kit_body.copy()
    name["name"] = kit_name
    return name

# Función de pruebas positivas
#
def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201 # Valor esperado = True / Positivo
    assert response.json()["name"] == kit_name # Valor esperado = True / Positivo

    # Verificar si realmente se registra el kit en la DB;
    # Solicitud->GET-> "var" se compara con la anterior Solicitud->POST-> "response"
    var = sender_stand_request.get_kit_table().text # variable "var" obtiene el texto de respuesta a la solicitud de la tabla "Kit" de BD
    # Se aplica .replace() para que la función de carácteres especiales se pueda leer correctamente
    assert str(response.json()["id"]) in var and response.json()["name"] in var.replace("\\","") # Valor esperado = True / Positivo

# Función de pruebas negativas
#
def negative_assert_code_400(kit_name):
    kit_body = get_kit_body(kit_name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400  # Valor esperado = True / Positivo
    # Confirmación de mensaje de error de ingreso de solicitud a la DB
    assert response.json()['message'] == 'Bad Request'

# 1° Función de prueba para un carácter (1)
# Ej. kit_body = { "name": "a"} -- Código de respuesta — 201
def test_create_kit_for_01_characters_success_response():
    return positive_assert("a")

# 2° Función de prueba para (511) carácteres
# Ej. kit_body = { "name": ... } -- Código de respuesta — 201
def test_create_kit_for_511_characters_success_response():
    positive_assert(data.kit_body["new_param_with_511_characters"])

# 3° Función de prueba para cero/vacio carácter
# Ej. kit_body = { "name": "" } -- Código de respuesta — 400
def test_create_kit_has_zero_characters_error_response():
    negative_assert_code_400("")

# 4° Función de prueba para (512) carácteres -> mayor de la permitida
# Ej. kit_body = { "name": "..." }   Código de respuesta — 400
def test_create_kit_para_512_characters_error_response():
    negative_assert_code_400(data.kit_body["new_param_with_512_characters"])

# 5° Función de prueba para caracteres especiales -> №%@&#
# Ej. kit_body = { "name": ""№%@"," }  Código de respuesta — 201
def test_create_kit_for_specials_characters_success_response():
    positive_assert('"N°%@",')

# 6° Función de prueba para espacios entre el nombre
# Ej. kit_body = { "name": " A Aaa " }  Código de respuesta — 201
def test_create_kit_has_spacie_characters_success_response():
    positive_assert(" A Aaa ")

# 7° Función de prueba para números en el nombre
# Ej. kit_body = { "name": "123" }  Código de respuesta — 201
def test_create_kit_has_numbers_characters_success_response():
    positive_assert("793")

# 8° Función de prueba donde NO se pasa parámetro "name"
# Ej. kit_body = { }  Código de respuesta — 400
def test_create_kit_has_empty_name_error_response():
    kit_body = {}
    negative_assert_code_400(kit_body)

# 9° Función de prueba con parámetro distinto a str (número)
# Ej. kit_body = { "name": 123 } -- Código de respuesta — 400
def test_create_kit_has_number_type_error_response():
    negative_assert_code_400(555)