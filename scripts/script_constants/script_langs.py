import  urllib.parse, http.client, json
from base64 import b64encode
import script_interface as interface

# Contants
api_url = '/api/lang/'


# insert_langs(c, headers), insert all langs in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_langs(c, headers):
    langs = ["en","es"]
    for lang in langs:
        params = json.dumps({'code': lang})
        interface.insert_data(c, api_url, params, headers)
