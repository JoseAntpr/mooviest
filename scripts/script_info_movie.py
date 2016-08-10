# import  urllib.parse, http.client, json
from base64 import b64encode
import psycopg2, urllib.request, urllib.parse, http.client, json

import interface
from script_tviso import script_celebrity as celebrity
from script_tviso import script_participation as participation
from script_tviso import script_movie as movie
from script_tviso import script_movie_lang as movie_lang
from script_tviso import script_rating as rating
from script_trakt_tv import script_celebrity as celebrity_trakt
from script_trakt_tv import script_movie_lang as movie_lang_trakt



def insert_celebrities_and_participations(celebrity_list, participation_list,db):
	for i in range(0,len(celebrity_list)):
		name = urllib.parse.quote_plus(celebrity_list[i]["name"])
		api_url_celebrity_by_name = "/api/celebrity_by_name/"+name+"/"
		api_url_celebrity = "/api/celebrity/"
		api_url_celebrity_lang = "/api/celebrity_lang/"
		api_url_participation = "/api/participation/"

		data = db.get_by_param(api_url_celebrity_by_name)
		results = data["results"]

		if len(results) == 0:
			print("result 0")
			born, address, biography = celebrity_trakt.get_info_celebrity(name)
			params = json.loads(celebrity_list[i])
			params["born"] = born
			params["address"] = address
			#Insert celebrity
			results = db.insert_data(api_url_celebrity, json.dumps(params))
			#Insert celebrity_lang
			params = json.dumps(
						{
							"celebrity": results["id"],
							"lang": interface.langs["en"],
							"biography": biography
						}
					)
			results = db.insert_data(api_url_celebrity_lang, params)
		else:
			results = results[0]

		print(results["id"])
		celebrity_id = results["id"]
		participation = json.loads(participation_list[i])
		participation['celebrity'] = celebrity_id
		data = db.insert_data(api_url_participation, json.dumps(participation))


# insert_info_tviso(c, headers), insert all info Tviso at DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_info(data, db):
    film = movie.insert_movie(db, data)
    movie_id = film["id"]

    film_lang = movie_lang.insert_movie_lang(db, data, movie_id)
    movie_name = film_lang["title"]
    print(movie_lang_trakt.insert_movie_lang("tt0167261"))


    # # Getters celebrities and participations
    # movie_id = 3
    # celebrity_list = celebrity.get_celebrities(data)
    # participation_list = participation.get_participations(data, movie_id)
	#
	#
    # # INSERTS celebrities and participations
    # insert_celebrities_and_participations(celebrity_list, participation_list, db)
	#
    # return movie_id, movie_name
