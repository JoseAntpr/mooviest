import json
from . import interface

def insert_rating(db, movie_id, source_id):

    url_movie = "/movies/" + source_id + "?extended=full"
    data = interface.get_info(url_movie)

    source = db.SOURCES["Trakt.tv"]
    sourceid = int(data["ids"]["trakt"])
    rating = int(data["rating"] * 10)
    count = int(data["votes"])

    rating = {
        "source": source,
        "movie": movie_id,
        "sourceid": sourceid,
        "rating": rating,
        "count": count
    }

    params = json.dumps(rating)

    return db.insert_data(db.API_URLS["rating"], params)
