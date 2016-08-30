import json
from . import interface

def insert_rating(db, movie_id, imdb_id):
    error_code = False
    error_message = ""
    url_movie = "/movies/" + imdb_id + "?extended=full"

    data = interface.get_info(url_movie)
    try:
        sourceid = int(data["ids"]["trakt"])
        rating = int(data["rating"] * 10)
        count = int(data["votes"])
    except:
        error_message = "Error get rating trakt.tv\n"
        error_code = True

    res = {}
    if not error_code:
        rating = json.dumps(
            {
                "source": db.SOURCES["Trakt.tv"],
                "movie": movie_id,
                "sourceid": sourceid,
                "name": "Trakt.tv",
                "rating": rating,
                "count": count
            }
        )

        try:
            res = db.insert_data(db.API_URLS["rating"], rating)
        except:
            error_message += "Error insert rating trakt.tv "+source_id+"\n"
            error_code = True

    return error_code, error_message, res
