# import  urllib.parse, http.client, json
from base64 import b64encode
import psycopg2, urllib.request, urllib.parse, http.client, json

import script_interface as interface
from . import script_celebrity as celebrity
from . import script_participation as participation
from . import script_movie as movie
from . import script_movie_lang as movie_lang
from . import script_rating as rating



def get_by_param(c, api_url, headers):
	c.request('GET', api_url, None, headers)
	res = c.getresponse()
	print(res.status, res.reason)
	data = res.read().decode("utf8")
	return json.loads(data)

def insert_celebrities_and_participations(celebrity_list, participation_list):
	for i in range(0,len(celebrity_list)):
		name = urllib.parse.quote_plus(celebrity_list[i]["name"])
		api_url_celebrity_by_name = "/api/celebrity_by_name/"+name+"/"
		api_url_celebrity = "/api/celebrity/"
		api_url_participation = "/api/participation/"
		c = http.client.HTTPConnection("127.0.0.1",8000)
		userAndPass = b64encode(b"admin:admin").decode("ascii")
		headers = { "Authorization" : "Basic " + userAndPass,"Content-type": "application/json" }

		data = get_by_param(c, api_url_celebrity_by_name, headers)
		results = data["results"]
		
		if len(results) == 0:
			print("result 0")
			params = json.dumps(celebrity_list[i])
			results = interface.insert_data(c, api_url_celebrity, params, headers)
		else:
			results = results[0]

		print(results["id"])
		celebrity_id = results["id"]
		participation = json.loads(participation_list[i])
		participation['celebrity'] = celebrity_id
		data = interface.insert_data(c, api_url_participation, json.dumps(participation), headers)

# insert_info_tviso(c, headers), insert all info Tviso at DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_info_tviso(c, headers, data):
    # film = movie.insert_movie(c, headers, data)
    # movie_id = film["id"]
    #
    # film_lang = movie_lang.insert_movie_lang(c, headers, data, movie_id)
    # movie_name = film_lang["title"]
    #
    # rating.insert_rating(c, headers, data, movie_id)

    # Getters celebrities and participations
    movie_id = 3
    celebrity_list = celebrity.get_celebrities(data)
    participation_list = participation.get_participations(data, movie_id)


    # INSERTS celebrities and participations
    insert_celebrities_and_participations(celebrity_list, participation_list)

    #return movie_id, movie_name
