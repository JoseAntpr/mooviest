import psycopg2, urllib.request, urllib.parse, http.client, json, time, predictionio, pytz
from base64 import b64encode
import interface
import interface_db

# Init DB
db = interface_db.DB("root", "root")
# event = ""

exporter = predictionio.FileExporter(file_name = "db_events.json")

for movie_id in range(1, 60):
    movie_info = db.search("/api/moviebasic/" + str(movie_id) + "/")
    event_properties = {
        "original_title": movie_info['original_title'],
        "genres": movie_info['genres'],
        "participations": movie_info['participations'],
        "runtime": movie_info['runtime'],
        "released": movie_info['released'],
        "movie_producer": movie_info['movie_producer'],
        "average": movie_info['average']
    }

    event_response = exporter.create_event(
        event = "$set",
        entity_type = "item",
        entity_id = str(movie_id),
        properties = event_properties
    )

exporter.close()
#
# for movie_id in range(1, 2):
#     movie_info = db.search("/api/moviebasic/" + str(movie_id) + "/")
#     genres = movie_info['genres']
#     participations = movie_info['participations']
#     original_title = movie_info['original_title']
#     runtime = movie_info['runtime']
#     released = movie_info['released']
#     movie_producer  = movie_info['movie_producer']
#     average = movie_info['average']
#
#     event = '{"event":"$set", "entityType":"item",'
#     event += '"entityId": "' + str(movie_id) + '",'
#     event += '"properties": {'
#     event += '"original_title": "' + original_title + '",'
#     event += '"genres": ' + str(genres) + ','
#     event += '"participations": ' + str(participations) + ','
#     event += '"runtime": ' + str(runtime) + ','
#     event += '"released": ' + str(released) + ','
#     event += '"movie_producer": "' + movie_producer + '",'
#     event += '"average": ' + str(average) + ''
#     event += '}}\n'

# movie_info = db.search("/api/moviebasic/" + "3/")
# print(movie_info['genres'])
# print(event)
