# Este archivo MAIN se debe ejecutar primero para crear un usuario
# Para visualizar la lista de los Kits en la BD; descomentar: var=función() y bucle for

import sender_stand_request

if __name__ == '__main__':

    # La función crea un usuario con datos fijados en data.py -> user_body{...}
    sender_stand_request.post_create_user()

#    Ejecutar solo sí hay datos en la tabla creados por el primer un usuario registrado (funcción previa).
#     var = sender_stand_request.get_kit_table()
#     print()
#     print("Lista de nombres de los Kits creados para un usuario:")
#     print()
#     for kit in var.json():
#         print(f'Kit-Name: {kit["name"]}')
