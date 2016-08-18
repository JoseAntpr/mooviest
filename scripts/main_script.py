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
from script_trakt_tv import script_rating as rating_trakt

# Get txts
lastline = interface.get_lastline(interface.lastline_txt)
actualline = lastline
ids = interface.get_ids(interface.datos_sin_numero_txt)
error_message = ""

# Generate token
auth_token = interface_tviso.get_token()

# Init DB
db = interface_db.DB("admin","admin")

# Insert constants
if (lastline == 0):
    constants.insert_constants(db)

# Bucle insert movies
for i in range(lastline, len(ids)):

    actualline = i
    error_code, error_message, data = interface_tviso.get_info_tviso(str(ids[i]).replace("\n",""), auth_token)
    error_head = "Movie idm: " + str(data["idm"]) + " - Script info_movie\n"

    if error_code != 0:
        if (error_code == 20 or error_code == 803):
            break
        error_message = error_head + error_message
        interface.save_log(interface.log_txt, error_message)
    else:
        # Info movie
        error_code_movie, msg, movie_id, movie_name, imdb_id = info_movie.insert_info(db, data)
        error_message += msg
        if not error_code_movie:
            # Insert ratings
            error_code, msg, res = rating_tviso.insert_rating(db, data, movie_id)
            error_message += msg

            error_code, msg, res = rating_trakt.insert_rating(db, movie_id, imdb_id)
            error_message += msg

            error_code, msg, res = rating_filmaffinity.insert_rating(db, movie_id, movie_name)
            error_message += msg

            error_code, msg, res_a, res_ex = rating_metacritic.insert_rating(db, movie_id, imdb_id)
            error_message += msg

            error_code, msg, res = rating_imdb.insert_rating(db, movie_id, imdb_id)
            error_message += msg

            error_code, msg, res_a, res_ex = rating_rotten_tomatoes.insert_rating(db, movie_id, imdb_id)
            error_message += msg

        if len(error_message) > 0:
            if not error_code_movie:
                error_message = error_head + "Mooviest id: " + str(movie_id)+" imdb_id: "+imdb_id+ "\n" + error_message
            interface.save_log(interface.log_txt, error_message+"\n")

interface.save_lastline(interface.lastline_txt, actualline+1)
# interface.send_mail()
