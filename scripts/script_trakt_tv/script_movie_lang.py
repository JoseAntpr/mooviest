import json
from . import interface

def insert_movie_lang(db, movie_id, source_id, country):
    error_code = False
    error_message = ""
    #Extract title,synopsis movie (English)
    title = ""
    synopsis = ""
    try:
        url_movie = "/movies/" + source_id + "?extended=full"
        data = interface.get_info(url_movie)
        title = data["title"]
        synopsis = data["overview"]
    except:
        error_message = "Error movie_lang trakt.tv\n"
    #Extract Image movie (English)
    image = ""
    try:
        url_image = "/movies/" + source_id + "?extended=images"
        data = interface.get_info(url_image)
        image = data["images"]["poster"]["medium"]
    except:
        error_message += "Error image movie trakt.tv\n"
        error_code_image = True

    params = json.dumps(
        {
            "movie": movie_id,
            "lang": db.LANGS['en'],
            "country": country,
            "title": title,
            "synopsis": synopsis,
            "image": image
        }
    )
    res = {}
    try:
        res = db.insert_data(db.API_URLS["movie_lang"], params)
    except:
        error_message += "Error insert movie_lang lang=EN trakt.tv\n"
        error_code = True

    return error_code, error_message, res
