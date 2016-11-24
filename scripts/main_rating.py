import psycopg2, urllib.request, urllib.parse, http.client, json, time
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

# # Get txts
lastline = interface.get_lastline(interface.lastline_txt)
actualline = lastline
# ids = interface.get_ids(interface.datos_sin_numero_txt)
error_message = ""
print(lastline)
#
# # Generate token
# auth_token = interface_tviso.get_token()

# Send first mail before clear log
interface.send_mail("First mail. Previous log attached - lastline: "+str(actualline)+" - "+str(time.strftime("%H:%M:%S")))

# Clear log
interface.clear_log()

# Init DB
db = interface_db.DB("admin","admin")
for i in range(lastline, 2998):
    error_message = ""
    actualline = i
    res = db.search("/api/rating/"+str(i)+"/")

    source = int(res["source"])
    if source == 5:
        movie_id = int(res["id"])
        imdb_id = res["sourceid"]
        print(movie_id, imdb_id)
        error_code, msg, res_a, res_ex = rating_rotten_tomatoes.insert_rating(db, movie_id, imdb_id)
        error_message += msg
        print(error_code, msg, res_a, res_ex)
        error_code, msg, res_a, res_ex = rating_metacritic.insert_rating(db, movie_id, imdb_id)
        error_message += msg
        print(error_code, msg, res_a, res_ex)
        error_head = "Mooviest id: " + str(movie_id) + " - Script info_movie\n"

        if len(error_message) > 0:
            interface.save_log(interface.log_txt, error_head + error_message + "\n")

    interface.save_lastline(interface.lastline_txt, actualline+1)

interface.send_mail("Error in main_script - lastline: "+str(actualline+1)+" - "+str(time.strftime("%H:%M:%S")))
