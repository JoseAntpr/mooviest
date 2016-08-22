# import  urllib.parse, http.client, json
from base64 import b64encode
import psycopg2, urllib.request, urllib.parse, http.client, json

from script_tviso import script_celebrity as celebrity_tviso
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
	error_code = False
	error_message = ""
	params = json.dumps(
		{
			"celebrity": celebrity_id,
			"lang": lang,
			"biography": biography
		}
	)
	res = {}
	try:
		res = db.insert_data(db.API_URLS["celebrity_lang"], params)
	except:
		error_message += "Error insert participation Tviso, celebrity_id:"+celebrity_id+"\n"
		error_code = True

	return error_code, error_message, res

# insert_celebrity_lang(db, celebrity_id, lang, biography), insert celebrity_lang
#			insert all celebrities and participations
#   Params
#       - db, Object DB
#		- celebrity_id, id celebrity
#		- lang, language info_movie
#		- biography, biography of celebrity
def insert_celebrity(db, celebrity):
	error_code = False
	error_message = ""
	res = {}
	try:
		res = db.insert_data(db.API_URLS["celebrity"], json.dumps(celebrity))
	except:
		error_message += "Error insert celebrity Tviso, name:"+celebrity["name"]+"\n"
		error_code = True

	return error_code, error_message, res

# insert_celebrity_lang(db, celebrity_id, lang, biography), insert celebrity_lang
#			insert all celebrities and participations
#   Params
#       - db, Object DB
#		- celebrity_id, id celebrity
#		- lang, language info_movie
#		- biography, biography of celebrity
def insert_participation(db, participation):
	error_code = False
	error_message = ""
	res = {}
	try:
		res = db.insert_data(db.API_URLS["participation"], json.dumps(participation))
	except:
		error_message += "Error insert participation Tviso, celebrity_id:"+participation["celebrity"]+"\n"
		error_code = True

	return error_code, error_message, res

# insert_celebrities_and_participations(db, celebrity_list, participation_list),
#			insert all celebrities and participations
#   Params
#       - db, Object DB
#		- celebrity_list, list celebrities of the current movie
#		- participation_list, associated participations
def insert_celebrities_and_participations(db, data, movie_id):
	error_message = ""
	celebrity_list, participation_list = celebrity_tviso.get_celebrities_and_participations(data, movie_id)
	for i in range(0,len(celebrity_list)):
	    name = urllib.parse.quote_plus(celebrity_list[i]["name"])

	    data = db.search(db.API_URLS["celebrity"]+"?search="+name)
	    results = data["results"]
	    if len(results) == 0:
		    celebrity = celebrity_list[i]
		    error_code_trakt, msg, born, address, biography = celebrity_trakt.get_info_celebrity(urllib.parse.unquote_plus(name))
		    error_message += msg
		    if not error_code_trakt:
			    celebrity["born"] = born
			    celebrity["address"] = address
			#Insert celebrity
		    error_code, msg, res_celebrity = insert_celebrity(db, celebrity)
		    error_message += msg
		    results = res_celebrity
			#Insert celebrity_lang(English)
		    if not (error_code_trakt or error_code):
		        error_code, msg, res_celebrity_lang = insert_celebrity_lang(db, results["id"], db.LANGS["en"], biography)
		        error_message += msg
	    else:
		    results = results[0]

	    participation = participation_list[i]
	    participation['celebrity'] = results["id"]
	    error_code, msg, res_participation = insert_participation(db, participation)
	    error_message += msg

	return error_message

# get_country(db, data, lang), return country id with lang
#   Params
#       - db, Object DB
#		- data, json info tviso
#		- lang, language info_movie
def get_country(db, data, lang):
    try:
        country = db.COUNTRIES[db.LANGS[lang]-1][str(data["country"][0])]
    except:
        country = None

    return country

# insert_info_tviso(c, headers), insert all info Tviso at DB
#   Params
#       - db, Object DB
#		- data, json info tviso
def insert_info(db, data):
	movie_id = 0
	movie_name = ""
	error_code = False
	error_message = ""
	released = 0
	try:
		imdb_id = data["imdb"]
	except:
		imdb_id = ""
		error_code =  True
		error_message = "No tiene id imdb_id"

	if not error_code:
		# Insert movie
		error_code, error_message, film = movie.insert_movie(db, data)
		if not error_code:
		    movie_id = film["id"]
		    movie_name = film["original_title"]
		    released = film["released"]
			# Insert movie_lang(Spanish)
		    country = get_country(db, data, "es")
		    error_code_movie_lang, msg, film_lang_es = movie_lang.insert_movie_lang(db, data, movie_id, country)
		    error_message += msg

			#Insert movie_lang(English)
		    country = get_country(db, data, "en")
		    error_code_trakt, msg, film_lang_en = movie_lang_trakt.insert_movie_lang(db, movie_id, imdb_id, country)
		    error_message += msg

			# Inserts celebrities and participations
		    msg = insert_celebrities_and_participations(db, data, movie_id)
		    error_message += msg

	return error_code, error_message, movie_id, movie_name, imdb_id, released
