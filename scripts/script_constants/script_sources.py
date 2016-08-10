import  urllib.parse, http.client, json
from base64 import b64encode
import interface

# Contants
api_url = '/api/source/'

# insert_sources(c, headers), insert all sources in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_sources(db):
    sources = ["FilmAffinity","Sensacine","Tviso","Track.tv","IMDb","Metacritic","RottenTomatoes","Letterboxd"]
    for source in sources:
        params = json.dumps({'name': source})
        db.insert_data(api_url, params)
