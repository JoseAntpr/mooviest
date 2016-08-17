import json
from . import interface

def insert_rating(db, movie_id, source_id):
    error_code = False
    error_message = ""
    res = {}
    
    try:
        url_movie = "/movies/" + source_id + "?extended=full"
        data = interface.get_info(url_movie)
        sourceid = int(data["ids"]["trakt"])
        rating = int(data["rating"] * 10)
        count = int(data["votes"])
    except:
        error_message = "Error get rating trakt.tv\n"
        error_code = True

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
            res = db.insert_data(db.API_URLS["rating"], params)
        except:
            error_message += "Error insert rating trakt.tv\n"
            error_code = True

    return error_code, error_message, res
