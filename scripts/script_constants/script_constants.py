import  urllib.parse, http.client, json
from base64 import b64encode

from . import script_langs as langs
from . import script_countries as countries
from . import script_genres as genres
from . import script_roles as roles
from . import script_sources as sources


# insert_constants(c, headers), insert all constanst in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_constants(db):
    langs.insert_langs(db)
    countries.insert_countries(db)
    genres.insert_genres(db)
    genres.insert_genres_lang(db)
    roles.insert_roles(db)
    roles.insert_roles_lang(db)
    sources.insert_sources(db)
