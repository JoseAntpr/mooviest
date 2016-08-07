import  urllib.parse, http.client, json
from base64 import b64encode
#

def insert_langs(c,userAndPass,headers):
    langs = ["en","es"]
    for lang in langs:
        params = urllib.parse.urlencode({'code': lang})
        c.request('POST', '/api/lang/', params, headers)
        res = c.getresponse()
        print(res.status, res.reason)
        data = res.read()
        print(data)
