import json
import script_interface as interface

def insert_rating(data, movie_id):
    source = interface.sources['Tviso']
    sourceid = int(data["idm"])
    rating = int(data["rating"]*10)
    count = int(data["ratings_num"])
    rating = {
        "source": source,
        "movie": movie_id,
        "sourceid": sourceid,
        "rating": rating,
        "count": count
    }

    return json.dumps(rating)
