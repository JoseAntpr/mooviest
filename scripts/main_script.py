import psycopg2, urllib.request, urllib.parse, http.client, json
from base64 import b64encode

import script_interface as interface
from script_constants import script_constants as constants
from script_tviso import script_tviso as tviso
# import scrappers.script_filmaffinity as filmaffinity


# Generación del token
auth_token = interface.get_token()
print(auth_token)


# Autenticación y generación de usuario para la llamada a la API
c = http.client.HTTPConnection("127.0.0.1",8000)
userAndPass = b64encode(b"jesus:root").decode("ascii")
headers = { "Authorization" : "Basic " + userAndPass,
            "Content-type": "application/json"}

idm = str(5411)

data, error = interface.get_info_tviso(idm, auth_token)

if error == 0:
    print(idm+' - Save succesfully')
    tviso.insert_info_tviso(c, headers, data)


# Insert constants en la BD (Solo la primera vez)
# if (last_id == 0){ ...insert constatns}
# constants.insert_constants(c, headers)


# # Bucle insert movies
# for i in range(last_id_tviso, max_id_tviso):
# 	idm = str(i)
#
# 	data, error = interface.get_info_tviso(idm, auth_token)
#
# 	if error != 0:
#         break
#
# 	print(idm+' - Save succesfully')
#     movie_id, movie_name = tviso.insert_info_tviso(c, headers, data)
#
#     filmaffinity.rating(c, headers, movie_id, movie_name)
