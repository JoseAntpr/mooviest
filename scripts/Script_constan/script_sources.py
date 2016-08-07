import  urllib.parse, http.client, json
from base64 import b64encode
#

def insert_sources(c,userAndPass,headers):
    sources = ["FilmAffinity","Sensacine","Tviso","Track.tv","IMDb","Metacritic","RottenTomatoes","Letterboxd"]
    for source in sources:
        params = urllib.parse.urlencode({'name': source})
        c.request('POST', '/api/source/', params, headers)
        #get the response back
        res = c.getresponse()
        print(res.status, res.reason)
        # at this point you could check the status etc
        # this gets the page text
        data = res.read()
        print(data)
