import urllib.request, urllib.parse, http.client, json
from base64 import b64encode
from . import interface as interface_trakt_tv

def insert_movie_lang(id_imdb):

    # Title and synopsis
    url_movie = "/movies/" + id_imdb + "?extended=full"

    interface_trakt_tv.c.request('GET', url_movie, None, interface_trakt_tv.headers)
    res = interface_trakt_tv.c.getresponse()
    data = json.loads(res.read().decode("utf8"))

    title = data["title"]
    synopsis = data["overview"]

    # Image
    url_image = "/movies/" + id_imdb + "?extended=images"

    interface_trakt_tv.c.request('GET', url_image, None, interface_trakt_tv.headers)
    res = interface_trakt_tv.c.getresponse()
    data = json.loads(res.read().decode("utf8"))

    image = data["images"]["poster"]["medium"]
