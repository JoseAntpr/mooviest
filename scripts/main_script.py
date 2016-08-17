import psycopg2, urllib.request, urllib.parse, http.client, json
from base64 import b64encode

import interface
import interface_db
import script_info_movie as info_movie
from script_constants import script_constants as constants
from script_tviso import interface as interface_tviso
from script_tviso import script_rating as rating_tviso
from scrappers import script_filmaffinity as rating_filmaffinity
from scrappers import script_metacritic as rating_metacritic
from scrappers import script_imdb as rating_imdb
from scrappers import script_rotten_tomatoes as rating_rotten_tomatoes
# Generación del token
# auth_token = interface_tviso.get_token()
# print(auth_token)
#
# db = interface_db.DB("admin","admin")
#
# constants.insert_constants(db)
#
# idm = str(5411)
#
# data = interface_tviso.get_info_tviso(idm, auth_token)
#
# if data["error"] == 0:
#     print(idm+' - Save succesfully')
#     #info_movie
#     movie_id, movie_name, imdb_id = info_movie.insert_info(db, data)
#     #insert rating
#     rating_tviso.insert_rating(db, data, movie_id)
#     rating_filmaffinity.insert_rating(db, movie_id, movie_name)
#     rating_metacritic.insert_rating(db, movie_id, imdb_id)
#     rating_imdb.insert_rating(db, movie_id, imdb_id)
#     error_code, error_message, url_rotten = rating_rotten_tomatoes.get_url_rottentomatoes_by_omdb(imdb_id)
#     rating_rotten_tomatoes.insert_rating(db, movie_id, url_rotten)

interface.save_lastline("lastline.txt",7)
l = interface.get_lastline("lastline.txt")
print(l)
ids = interface.get_ids("datos_sin_numero.txt")
print(ids[l])
# Insert constants en la BD (Solo la primera vez)
# if (last_id == 0){ ...insert constatns}
# constants.insert_constants(c, headers)


# Bucle insert movies
# for i in range(last_id_tviso, max_id_tviso):
# 	idm = str(i)
#
# 	data = interface.get_info_tviso(idm, auth_token)
#
# 	if (data["error"] == 20 || data["error"] == 803):
#         break
#     elif data["error"] == 0:
#         #Insert info movie id = i
#         movie_id, movie_name = info_movie.insert_info(c, headers, data)
#         #Insert ratings
#         rating_tviso.insert_rating(db, data, movie_id)
#         rating_filmaffinity.insert_rating(db, movie_id, movie_name)
