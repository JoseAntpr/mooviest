from . import interface
s = "mierda"
def insert_movie_lang(id_imdb):
    # Title and synopsis
    url_movie = "/movies/" + id_imdb + "?extended=full"

    data = interface.get_info(url_movie)
    title = data["title"]
    synopsis = data["overview"]

    # Image
    url_image = "/movies/" + id_imdb + "?extended=images"

    data = interface.get_info(url_image)
    image = data["images"]["poster"]["medium"]

    return title, synopsis, image
