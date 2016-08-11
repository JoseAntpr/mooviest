import  urllib.parse, http.client, json
from base64 import b64encode
import interface

# insert_roles(c, headers), insert all roles in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_roles(db):
    roles = ["actor","director","producer","writer","composer"]
    for role in roles:
        params = json.dumps({'code': role})
        db.insert_data(api_url_roles, params)


# insert_roles_lang(c, headers), insert all roles_lang in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_roles_lang(db):
    roles = [["Actor","Director","Producer","Writer","Composer"],
            ["Actor","Director","Productor","Escritor","Compositor"]]

    for i in range(0,len(roles)):
        for j in range(0,len(roles[0])):
            params = json.dumps({
                'role': (j+1),
                'lang': (i+1),
                'name': roles[i][j]
            })
            db.insert_data(api_url_roles_lang, params)
