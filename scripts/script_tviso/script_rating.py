import json

def insert_rating(db, data, movie_id):
    source = db.SOURCES['Tviso']
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
    db.insert_data(db.API_URLS["rating"], params)
