import  urllib.parse, http.client, json
from base64 import b64encode
import script_countries as countries
import script_genres as genres
import script_langs as langs
import script_roles as roles
import script_sources as sources

# insert_constants(c, headers), insert all constanst in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_constants(c,headers):
    langs.insert_langs(c,headers)
    countries.insert_countries(c, headers)
    genres.insert_genres(c, headers)
    genres.insert_genres_lang(c, headers)
    roles.insert_roles(c, headers)
    roles.insert_roles_lang(c, headers)
    sources.insert_sources(c, headers)
