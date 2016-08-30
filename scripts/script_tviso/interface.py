import urllib.request, http.client, json
# Constants Tviso
id_api = '3504'
secret = 'bhRNt7TaHhuVcKxExK3n'
mediaType = "2"


GENRES_JSON = {
				'action':      1,  'comedy':    2,  'family':    3,
				'history':     4,  'mystery':   5,  'sci-fi':    6,
				'war':         7,  'adventure': 8,  'crime':     9,
				'fantasy':     10, 'horror':    11, 'news':      12,
				'sport':       13, 'western':   14, 'animation': 15,
				'documentary': 16, 'film-noir': 17, 'music':     18,
				'drama':       19, 'musical':   20,	'romance':   21,
				'thriller':    22, 'reallity':  23, 'biography': 24,
				'short':	   25, 'adult':     26, 'talk-show': 27,
				'reality-tv':  28, 'game-show': 29
			}
ROLES = {
			"actor": 1, "director": 2, "producer": 3,
			"writer": 4 ,"composer": 5
		}

def get_token():
	return json.loads(urllib.request.urlopen('https://api.tviso.com/auth_token?id_api=' + id_api + '&secret=' + secret).read().decode('utf8'))["auth_token"]


# get_info_tviso, return data format json, of the media with idm
#   Params
#       - idm, id(Tviso) of the media
#       - auth_token, token of the API Tviso, generate with the data mooviest
#       - mediaType, type of media, 1-Serie/2-Movie/3-TvShow/4-Docu/5-Capitulo
#   if all ok, data["error"] == 0

def get_info_tviso(idm, auth_token):
	url = "https://api.tviso.com/media/full_info?auth_token=" + auth_token + "&idm=" + idm  + "&mediaType=" + mediaType
	error_message = ""
	data = {}

	try:
		response = urllib.request.urlopen(url)
		data = json.loads(response.read().decode("utf8"))
		error = data["error"]
	except:
		error_message = "Error call get_info_tviso url: " + url + "\n"
		error = 2

	if error == 1:
		error_message = "error: Auth token\n"
		auth_token = get_token()

	elif(error == 9 or error == 50):
		error_message = "error: Media type\n"

	elif error == 10:
		error_message = "error: Idm\n"

	elif error == 20:
		error_message = "error: Quota exceeded\n"

	elif error == 502:
		error_message = "error: Response timeout or internet connection is not available\n"

	elif error == 803:
		error_message = "error: Media limit reached\n"

	return error, error_message, auth_token, data
