import json
from . import interface

# MOVIE model
def insert_movie(db, data):
    runtime = int(data["runtime"])
    released = int(data["year"])
    imdb = str(data["imdb"])
    original_title=str(data["original_name"])

    movie_producer_list = []
    for produce in data["produce"]:
        movie_producer_list.append(produce["name"])

    movie_producer = ' | '.join(movie_producer_list)

    genres = []
    for i, genre in enumerate(data["genres"]):
        genres.append(interface.GENRES_JSON[str(genre.lower())])

    movie = {
        "genres": genres,
        "emotions": [],
        "saga": None,
        "original_title": original_title,
        "runtime": runtime,
        "released": released,
        "movie_producer": movie_producer,
        "saga_order": 1,
        "average": 0.0
    }

    params = json.dumps(movie)
    return db.insert_data(db.API_URLS["movie"], params)
