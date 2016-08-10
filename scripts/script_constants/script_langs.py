import  urllib.parse, http.client, json
from base64 import b64encode
import interface

# Contants
api_url = '/api/lang/'


# insert_langs(c, headers), insert all langs in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_langs(db):
    langs = ["en","es"]
    for lang in langs:
        params = json.dumps({'code': lang})
        db.insert_data(api_url, params)
