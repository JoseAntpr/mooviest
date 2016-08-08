import  urllib.parse, http.client, json
from base64 import b64encode

movie_json = json.dumps({
    "genres": [8],
    "emotions": [],
    "saga": None,
    "original_title": "mierda seca3",
    "runtime": None,
    "released": None,
    "image": "",
    "movie_producer": "mierda producer",
    "saga_order": 2,
    "average": 10
}, sort_keys=True)

c = http.client.HTTPConnection("127.0.0.1",8000)
userAndPass = b64encode(b"admin:admin").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass,
            "Content-type": "application/json",
            "Accept": "application/json" }

c.request('POST', '/api/movie/', movie_json, headers)
res = c.getresponse()
print(res.status, res.reason)
data = res.read()
print(data)
