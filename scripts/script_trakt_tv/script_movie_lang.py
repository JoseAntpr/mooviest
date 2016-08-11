import json
from . import interface

def insert_movie_lang(db, movie_id, source_id, country):
    # Title and synopsis
    url_movie = "/movies/" + source_id + "?extended=full"

    data = interface.get_info(url_movie)
    title = data["title"]
    synopsis = data["overview"]

    # Image
    url_image = "/movies/" + source_id + "?extended=images"

    data = interface.get_info(url_image)
    image = data["images"]["poster"]["medium"]

    try:
        country =  db.COUNTRIES[db.LANGS["en"]-1][str(country)]
    except TypeError:
        country = None

    movie_lang = {
        "movie": movie_id,
        "lang": db.LANGS['en'],
        "country": country,
        "title": title,
        "synopsis": synopsis,
        "image": image
    }
    params = json.dumps(movie_lang)

    return db.insert_data(db.API_URLS["movie_lang"], params)
