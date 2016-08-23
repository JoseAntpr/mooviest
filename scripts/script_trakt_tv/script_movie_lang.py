import json
from . import interface

def insert_movie_lang(db, movie_id, source_id, country):
    error_code = False
    error_code_data = False
    error_code_image = False
    error_message = ""
    res = {}

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
        error_code_data = True

    if not error_code_data:
        #Extract Image movie (English)
        image = ""
        try:
            url_image = "/movies/" + source_id + "?extended=images"
            data = interface.get_info(url_image)
            image = data["images"]["poster"]["medium"]
        except:
            error_message += "Error image movie trakt.tv\n"
            error_code_image = True

        if not error_code_image:
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

            res = db.insert_data(db.API_URLS["movie_lang"], params)
            try:
                res["id"]
            except:
                error_message += "Error insert movie_lang lang=EN trakt.tv" + str(params) + "\n"
                error_code = True

    return error_code, error_message, res
