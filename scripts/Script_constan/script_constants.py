import  urllib.parse, http.client, json
from base64 import b64encode
import script_countries as countries
import script_genres as genres
import script_langs as langs
import script_roles as roles
import script_sources as sources

# Autenticación y generación de usuario para la llamada a la API
c = http.client.HTTPConnection("127.0.0.1",8000)
userAndPass = b64encode(b"admin:admin").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass,
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "application/json" }

langs.insert_langs(c,headers)
countries.insert_countries(c, headers)
genres.insert_genres(c, headers)
genres.insert_genres_lang(c, headers)
roles.insert_roles(c, headers)
roles.insert_roles_lang(c, headers)
sources.insert_sources(c, headers)
