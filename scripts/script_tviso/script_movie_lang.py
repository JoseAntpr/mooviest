import json
from . import interface

# insert_movie_lang(db, data, movie_id, country), insert movie_lang lang=ES in DB
#   Params
#       - db, interface db
#       - data, json data of Tviso
#       - movie_id, id of the movie in mooviest db
#       - country, country parsed
def insert_movie_lang(db, data, movie_id, country):
    error_code = False
    error_message = ""
    res = {}

    try:
        title = str(data["name"])
        synopsis = str(data["plot"])
        image = str(data["images"]["poster"])
    except:
        error_code = True
        error_message = "Error GET data movie_lang lang=ES\n"

    if not error_code:
        movie_lang = {
            "movie": movie_id,
            "lang": db.LANGS["es"],
            "country": country,
            "title": title,
            "synopsis": synopsis,
            "image": image
        }
        params = json.dumps(movie_lang)
        try:
            res = db.insert_data(db.API_URLS["movie_lang"], params)
        except:
            error_code = True
            error_message += "Error INSERT movie_lang lang=ES\n"

    return error_code, error_message, res
