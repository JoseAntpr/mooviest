import json
from . import interface

# insert_movie(db, data), insert movie in DB
#   Params
#       - db, interface db
#       - data, json data of Tviso
def insert_movie(db, data):
    error_code = False
    error_message = ""
    res = {}

    try
        runtime = int(data["runtime"])
        released = int(data["year"])
        imdb = str(data["imdb"])
        original_title=str(data["original_name"])
        produces = data["produce"]
        genres = data["genres"]
    except:
        error_code = True
        error_message = "Error GET data movie\n"

    if not error_code:

        movie_producer_list = []
        for produce in produces:
            movie_producer_list.append(produce["name"])

        movie_producer = ' | '.join(movie_producer_list)

        genres_list = []
        for genre in genres:
            genres_list.append(interface.GENRES_JSON[str(genre.lower())])

        movie = {
            "genres": genres_list,
            "emotions": [],
            "saga": None,
            "original_title": original_title,
            "runtime": runtime,
            "released": released,
            "movie_producer": movie_producer,
            "saga_order": 1,
            "average": 0.0
        }
        params = json.dumps(movie)

        try
            res = db.insert_data(db.API_URLS["movie"], params)
        except:
            error_code = True
            error_message += "Error INSERT movie\n"

    return error_code, error_message, res
