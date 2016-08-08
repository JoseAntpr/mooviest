import  urllib.parse, http.client, json
from base64 import b64encode
import script_movie as movie
import script_movie_lang as movie_lang
import script_rating as rating

# insert_info_tviso(c, headers), insert all info Tviso at DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_info_tviso(c, headers, data):
    film = movie.insert_movie(c, headers, data)
    movie_id = film["id"]

    film_lang = movie_lang.insert_movie_lang(c, headers, data, movie_id)
    movie_name = film_lang["title"]

    rating.insert_rating(c, headers, data, movie_id)

    # INSERT celebrity

    # INSERT participation

    return movie_id, movie_name
