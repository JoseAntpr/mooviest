import urllib.request, http.client, json
from base64 import b64encode

class DB:
    # Constants app
    LANGS = { "en": 1, "es": 2}

    SOURCES = {
    	"FilmAffinity":		1,
    	"Sensacine":		2,
     	"Tviso":			3,
    	"Trakt.tv":			4,
    	"IMDb":				5,
    	"Metacritic":		6,
    	"RottenTomatoes":	7,
    	"Letterboxd":		8
    }

    COUNTRIES = [
    	{
    		"ES": 1,"DE": 2,"IT": 3,"FR": 4,"GB": 5,
    		"US": 6,"AR": 7,"MX": 8,"XX": 9
    	},{
    		"ES": 10,"DE": 11,"IT": 12,"FR": 13,"GB": 14,
    		"US": 15,"AR": 16,"MX": 17,"XX": 18
    	}
    ]

    API_URLS = {
        "rating": "/api/rating/",
        "country": "/api/country/",
        "genre": "/api/genre/",
        "genre_lang": "/api/genre_lang/",
        "lang": "/api/lang/",
        "role": "/api/role/",
        "role_lang": "/api/role_lang/",
        "source": "/api/source/",
        "movie": "/api/movie/",
        "movie_lang": "/api/movie_lang/"
    }

    connection = ""
    headers = ""

    def __init__(self,user,password):
        # Autenticación y generación de usuario para la llamada a la API
        userAndPass = b64encode(str(user+":"+password).encode("utf-8")).decode("ascii")
        self.connection = http.client.HTTPConnection("127.0.0.1",8000)
        self.headers = { "Authorization" : "Basic " + userAndPass,
                    "Content-type": "application/json"}

    def insert_data(self,api_url, js):
    	self.connection.request('POST', api_url, js, self.headers)
    	res = self.connection.getresponse()
    	print(res.status, res.reason)
    	data = res.read().decode("utf8")

    	return json.loads(data)

    def get_by_param(self,api_url):
    	self.connection.request('GET', api_url, None, self.headers)
    	res = self.connection.getresponse()
    	print(res.status, res.reason)
    	data = res.read().decode("utf8")
    	return json.loads(data)
