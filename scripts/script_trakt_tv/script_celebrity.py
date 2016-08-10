import urllib.request, urllib.parse, http.client, json
from base64 import b64encode

def get_info_celebrity(person):

    url_person = "/people/" + person + "?extended=full"

    interface_trakt_tv.c.request('GET', url_person, None, interface_trakt_tv.headers)
    res = interface_trakt_tv.c.getresponse()
    data = json.loads(res.read().decode("utf8"))

    born = data["birthday"]
    address = data["birthplace"]
    biography = data["biography"]

    return born, address, biography
