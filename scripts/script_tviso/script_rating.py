import json
import script_interface as interface

# Contants
api_url = '/api/rating/'

def insert_rating(c, headers, data, movie_id):
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

    params = json.dumps(rating)

    interface.insert_data(c, api_url, params, headers)
