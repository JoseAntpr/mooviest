import json
import ../script_interface as interface

# MOVIE_LANG model
def parser_movie_lang(data, movie_id):

    title = str(data["name"])
    synopsis=str(data["plot"])

    country = None
    try:
        country =  interface.countries[data["country"][0]]
    except TypeError:
        country = None

    movie_lang = {
        "movie": movie_id,
        "lang": interface.langs['es'],
        "country": country,
        "title": title,
        "synopsis": synopsis
    }

    return json.dumps(movie_lang)
