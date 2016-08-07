import  urllib.parse, http.client, json
from base64 import b64encode

#

def insert_countries(c,userAndPass,headers):
	countries=[
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
			params = urllib.parse.urlencode(
				{
                    "lang": (i+1),
                    "name": countries[i][j][0],
                    "code": countries[i][j][1]
                }
			)

			c.request('POST', '/api/country/', params, headers)
			#get the response back
			res = c.getresponse()
			print(res.status, res.reason)
			# at this point you could check the status etc
			# this gets the page text
			data = res.read()
