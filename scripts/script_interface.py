import psycopg2, urllib.request, urllib.parse, http.client, json
from base64 import b64encode

langs = { "en": 1, "es": 2}

countries=[
	{
		'ES': 1,
		'DE': 2,
		'IT': 3,
		'FR': 4,
		'GB': 5,
		'US': 6,
		'AR': 7,
		'MX': 8,
		'XX': 9
	},
	{
		'ES': 10,
		'DE': 11,
		'IT': 12,
		'FR': 13,
		'GB': 14,
		'US': 15,
		'AR': 16,
		'MX': 17,
		'XX': 18
	}
]

def insert_data(c, api_url, js, headers):

    c.request('POST', api_url, js, headers)
    res = c.getresponse()
    print(res.status, res.reason)
    data = res.read()
    print(data)
