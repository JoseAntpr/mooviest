import json
from . import interface

# insert_movie(genre), insert new genre and genre_lang (en)
#   Params
#       - genre, genre.lower()
def insert_new_genre(db, genre_name):
    error_code =  False
    error_message = "Try to insert genre " + genre_name+"\n"
    error_message += "Remember to update script_tviso/interface.py/GENRES_JSON and script_constants/script_genres.py/genres and genres_lang\n"

    # Insert genre in DB
    params = json.dumps({'code': genre_name})
    data = db.insert_data(db.API_URLS["genre"], params)

    try:
        genre_id = data["id"]
        error_message += "Genre: " + genre_name + " added to DB successfully\n"
        # Update interface.GENRES_JSON
        interface.GENRES_JSON.update({genre_name : len(interface.GENRES_JSON)+1})
    except:
        error_code = True
        error_message += "Error to insert genre: " + genre_name + " in DB\n"

    if not error_code:
        # Insert genre_lang (en) in DB
        genre_lang = genre_name.capitalize()
        params = json.dumps(
            {
                "genre": genre_id,
                "lang": 1,
                "name": genre_lang
            }
        )
        data = db.insert_data(db.API_URLS["genre_lang"], params)

        try:
            data["id"]
            error_message += "Genre_lang: " + genre_lang + " added to DB successfully\n"
        except:
            error_message += "Error to insert genre_lang: " + genre_lang + " in DB\n"


    return error_code, error_message

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
            error_c = False
            if str(genre.lower()) != "":
                try:
                    interface.GENRES_JSON[str(genre.lower())]
                except:
                    error_c, msg = insert_new_genre(db, genre.lower())
                    error_message += msg
                if not error_c:
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
