# import  urllib.parse, http.client, json
from base64 import b64encode
import psycopg2, urllib.request, urllib.parse, http.client, json

import interface
from script_tviso import script_celebrity as celebrity_tviso
from script_tviso import script_participation as participation_tviso
from script_tviso import script_movie as movie
from script_tviso import script_movie_lang as movie_lang
from script_tviso import script_rating as rating
from script_trakt_tv import script_celebrity as celebrity_trakt
from script_trakt_tv import script_movie_lang as movie_lang_trakt


# insert_celebrity_lang(db, celebrity_id, lang, biography), insert celebrity_lang
#			insert all celebrities and participations
#   Params
#       - db, Object DB
#		- celebrity_id, id celebrity
#		- lang, language info_movie
#		- biography, biography of celebrity
def insert_celebrity_lang(db, celebrity_id, lang, biography):
	params = json.dumps(
				{
					"celebrity": celebrity_id,
					"lang": lang,
					"biography": biography
				}
			)
	return db.insert_data(db.API_URLS["celebrity_lang"], params)

# insert_celebrities_and_participations(db, celebrity_list, participation_list),
#			insert all celebrities and participations
#   Params
#       - db, Object DB
#		- celebrity_list, list celebrities of the current movie
#		- participation_list, associated participations
def insert_celebrities_and_participations(db, data, movie_id):
    celebrity_list = celebrity_tviso.get_celebrities(data)
    participation_list = participation_tviso.get_participations(data, movie_id)

    for i in range(0,len(celebrity_list)):
	    name = urllib.parse.quote_plus(celebrity_list[i]["name"])
	    data = db.search(db.API_URLS["celebrity"]+"?search="+name+"/")
	    results = data["results"]
	    ok = True
	    if len(results) == 0:
		    try:
			    born, address, biography = celebrity_trakt.get_info_celebrity(urllib.parse.unquote_plus(name))
			    params = celebrity_list[i]
			    params["born"] = born
			    params["address"] = address
				#Insert celebrity
			    results = db.insert_data(db.API_URLS["celebrity"], json.dumps(params))
				#Insert celebrity_lang(English)
			    results = insert_celebrity_lang(db, results["id"], db.LANGS["en"], biography)
		    except:
			    print("No se ha insertado la celebrity "+name)
			    ok = False
	    else:
		    results = results[0]

	    if ok:
		    participation = json.loads(participation_list[i])
		    participation['celebrity'] = results["id"]
		    data = db.insert_data(db.API_URLS["participation"], json.dumps(participation))


# insert_info_tviso(c, headers), insert all info Tviso at DB
#   Params
#       - db, Object DB
#		- data, json info tviso
def insert_info(db, data):
    film = movie.insert_movie(db, data)
    movie_id = film["id"]
	#Insert movie_lang(Spanish)
    film_lang = movie_lang.insert_movie_lang(db, data, movie_id)
    movie_name = film_lang["title"]
	#Insert movie_lang(English)
    imdb_id = data["imdb"]
    movie_lang_trakt.insert_movie_lang(db, movie_id, imdb_id, data["country"][0])

	# Inserts celebrities and participations
    insert_celebrities_and_participations(db, data, movie_id)

    return movie_id, movie_name, imdb_id
