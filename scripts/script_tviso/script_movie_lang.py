import json
from . import interface

# MOVIE_LANG model
def insert_movie_lang(db, data, movie_id):

    title = str(data["name"])
    synopsis = str(data["plot"])
    image = str(data["images"]["poster"])

    country = None
    try:
        country =  db.COUNTRIES[db.LANGS['es']-1][data["country"][0]]
    except TypeError:
        country = None

    movie_lang = {
        "movie": movie_id,
        "lang": db.LANGS["es"],
        "country": country,
        "title": title,
        "synopsis": synopsis,
        "image": image
    }
    params = json.dumps(movie_lang)
    return db.insert_data(db.API_URLS["movie_lang"], params)
