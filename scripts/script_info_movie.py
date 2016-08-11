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
		print(results)
		ok = True
		if len(results) == 0:
			print("result 0")
			try:
				born, address, biography = celebrity_trakt.get_info_celebrity(urllib.parse.unquote_plus(name))
				print(celebrity_list[i])
				params = celebrity_list[i]
				params["born"] = born
				params["address"] = address
				print(params)
				#Insert celebrity
				results = db.insert_data(api_url_celebrity, json.dumps(params))
				#Insert celebrity_lang
				params = json.dumps(
							{
								"celebrity": results["id"],
								"lang": db.LANGS["en"],
								"biography": biography
							}
						)
				results = db.insert_data(api_url_celebrity_lang, params)
			except:
				print("No se ha insertado la celebrity "+name)
				ok = False

		else:
			results = results[0]

		if ok:
			print(results)
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

    movie_lang_trakt.insert_movie_lang(db, movie_id, data["imdb"],data["country"][0])


    # Getters celebrities and participations
    celebrity_list = celebrity.get_celebrities(data)
    participation_list = participation.get_participations(data, movie_id)


    # INSERTS celebrities and participations
    insert_celebrities_and_participations(celebrity_list, participation_list, db)

    return movie_id, movie_name
