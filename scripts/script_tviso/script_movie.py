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

    try:
        original_title=str(data["original_name"])
    except:
        error_code = True
        error_message = "Error GET data movie\n"

    if not error_code:

        try:
            runtime = int(data["runtime"])
        except:
            runtime = 0

        try:
            released = int(data["year"])
        except:
            released = 0

        try:
            produces = data["produce"]
        except:
            produces = []

        try:
            genres = data["genres"]
        except:
            genres = []

        movie_producer_list = []
        for produce in produces:
            movie_producer_list.append(produce["name"])

        if (len(movie_producer_list) > 0) :
            movie_producer = ' | '.join(movie_producer_list)
        else:
            movie_producer = ""

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


        res = db.insert_data(db.API_URLS["movie"], params)
        try:
            res["id"]
        except:
            error_code = True
            error_message += "Error INSERT movie: " + str(res) + "\n"

    return error_code, error_message, res
