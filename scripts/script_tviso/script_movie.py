import json
import script_interface as interface

# Contants
api_url = '/api/movie/'

# MOVIE model
def insert_movie(c, headers, data):

    genres_json={'action':   1,
			'comedy':        2,
			'family':        3,
			'history':       4,
			'mystery':       5,
			'sci-fi':        6,
			'war':           7,
			'adventure':     8,
			'crime':         9,
			'fantasy':       10,
			'horror':        11,
			'news':          12,
			'sport':         13,
			'western':       14,
			'animation':     15,
			'documentary':   16,
			'film-noir':     17,
			'music':         18,
			'drama':         19,
			'musical':       20,
			'romance':       21,
			'thriller':      22,
			'reallity':      23
    }

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
        genres.append(genres_json[str(genre.lower())])

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

    return interface.insert_data(c, api_url, params, headers)
