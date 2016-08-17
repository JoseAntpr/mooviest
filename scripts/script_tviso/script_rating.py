import json

# insert_rating(db, data, movie_id), insert rating in DB
#   Params
#       - db, interface db
#       - data, json data of Tviso
#       - movie_id, id of the movie in mooviest db
def insert_rating(db, data, movie_id):
    error_code = False
    error_message = ""
    res = {}

    try:
        source = db.SOURCES['Tviso']
        sourceid = int(data["idm"])
        rating = int(data["rating"]*10)
        count = int(data["ratings_num"])
        rating = {
            "source": source,
            "movie": movie_id,
            "sourceid": sourceid,
            "name": "Tviso",
            "rating": rating,
            "count": count
        }

        params = json.dumps(rating)
        res = db.insert_data(db.API_URLS["rating"], params)
    except:
        error_code = True
        error_message = "Error INSERT rating Tviso

    return error_code, error_message, res
