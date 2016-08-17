import json
from . import interface

def insert_rating(db, movie_id, source_id):
    error_code = False
    error_message = ""

    source = db.SOURCES["Trakt.tv"]
    sourceid = 0
    rating = 0
    count = 0
    try:
        url_movie = "/movies/" + source_id + "?extended=full"
        data = interface.get_info(url_movie)
        sourceid = int(data["ids"]["trakt"])
        rating = int(data["rating"] * 10)
        count = int(data["votes"])
    except:
        error_message = "Error rating trakt.tv\n"

    rating = json.dumps(
        {
            "source": source,
            "movie": movie_id,
            "sourceid": sourceid,
            "rating": rating,
            "count": count
        }
    )
    res = {}
    try:
        res = db.insert_data(db.API_URLS["rating"], params)
    except:
        error_message += "Error insert rating trakt.tv\n"
        error_code = True

    return error_code, error_message, res
