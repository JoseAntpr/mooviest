import psycopg2, urllib.request, urllib.parse, http.client, json, time
from base64 import b64encode
import interface
import interface_db

# Init DB
db = interface_db.DB("root", "root")

#for movie_id in range(0, 60):
#    movie_info = db.search(db.API_URLS["movie"] + movie_id + "/")
#    genres =
#    participations =
#    original_title =
#    runtime =
#    released =
#    movie_producer =
#    average =
#    event = "{'event':'$set', 'entityType':'item', 'entityId': '"
#                + movie_id + "', 'properties': {'original_title': '"
#                + original_title + "', 'genres': '"
#                + genres + "', 'participations': '"
#                + runtime + "', 'released': '"
#                + released + "', 'movie_producer': '"
#                + movie_producer + "', 'average': '"
#                + average + "'}" + "}" + "\n"

print(db.search(db.API_URLS["movie"] + "3/"))
