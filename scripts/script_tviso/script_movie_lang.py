import json
from . import interface

# Contants
api_url = '/api/movie_lang/'

# MOVIE_LANG model
def insert_movie_lang(db, data, movie_id):

    title = str(data["name"])
    synopsis=str(data["plot"])
    image=str(data["images"]["poster"])

    country = None
    try:
        country =  db.COUNTRIES[db.LANGS['es']-1][data["country"][0]]
    except TypeError:
        country = None

    # FALTA AÑADIR CUANDO ESTÉ EN EL MODELO
    # "image": image,
    movie_lang = {
        "movie": movie_id,
        "lang": db.LANGS['es'],
        "country": country,
        "title": title,
        "synopsis": synopsis,
        "image": image
    }
    params = json.dumps(movie_lang)

    return db.insert_data(api_url, params)
