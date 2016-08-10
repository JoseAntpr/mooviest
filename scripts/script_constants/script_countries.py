import  urllib.parse, http.client, json
from base64 import b64encode
import script_interface as interface

# Contants
api_url = '/api/country/'

# insert_countries(c, headers), insert all countries in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_countries(c, headers):
	countries = [
        [
            ['Spain','ES'],
    		['Germany','DE'],
    		['Italy','IT'],
            ['France','FR'],
            ['Great Britain','GB'],
            ['United States','US'],
            ['Argentina','AR'],
            ['Mexico','MX'],
            ['Global','XX']
		],
		[
            ['España','ES'],
    		['Alemania','DE'],
    		['Italia','IT'],
            ['Francia','FR'],
            ['Gran Bretaña','GB'],
            ['Estados Unidos','US'],
            ['Argentina','AR'],
            ['México','MX'],
            ['Global','XX']
		]
    ]

	for i in range(0,len(countries)):
		for j in range(0,len(countries[0])):
			params = json.dumps(
				{
                    "lang": (i+1),
                    "name": countries[i][j][0],
                    "code": countries[i][j][1]
                }
			)
			interface.insert_data(c, api_url, params, headers)
