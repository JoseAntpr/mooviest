import json
import script_interface as interface

# Contants
api_url = '/api/movie_lang/'

# MOVIE_LANG model
def insert_movie_lang(c, headers, data, movie_id):

    title = str(data["name"])
    synopsis=str(data["plot"])
    image=str(data["images"]["poster"])

    country = None
    try:
        country =  interface.countries[interface.langs['es']-1][data["country"][0]]
    except TypeError:
        country = None

    # FALTA AÑADIR CUANDO ESTÉ EN EL MODELO
    # "image": image,
    movie_lang = {
        "movie": movie_id,
        "lang": interface.langs['es'],
        "country": country,
        "title": title,
        "synopsis": synopsis
    }
    params = json.dumps(movie_lang)

    return interface.insert_data(c, api_url, params, headers)
