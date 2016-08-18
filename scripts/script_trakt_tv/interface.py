import http.client, json, unicodedata

trakt_api_version = 2
client_id = "b62243ebed0a24da0d44377a0ac1d4cc51a0de77a8be36a0bcbf67ba2142026d"

c = http.client.HTTPSConnection("api.trakt.tv", None)
headers = { "Content-type": "application/json",
            "trakt-api-version" : trakt_api_version ,
            "trakt-api-key" : client_id}

def get_info(url):
    res = {}
    try:
        c.request('GET', url, None, headers)
        res = c.getresponse()
        res = json.loads(res.read().decode("utf8"))
    except:
        res = {}
    return res

def strip_accents(text):
    s = ''.join((c for c in unicodedata.normalize('NFD',text) if unicodedata.category(c) != 'Mn'))
    return s
