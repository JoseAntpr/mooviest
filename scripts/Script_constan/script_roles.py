import  urllib.parse, http.client, json
from base64 import b64encode
#

def insert_roles(c, headers):
    roles = ["actor","director","producer","writer","composer"]
    for role in roles:
        params = urllib.parse.urlencode({'code': role})
        c.request('POST', '/api/role/', params, headers)
        #get the response back
        res = c.getresponse()
        print(res.status, res.reason)
        # at this point you could check the status etc
        # this gets the page text
        data = res.read()
        print(data)

def insert_roles_lang(c, headers):
    roles = [["Actor","Director","Producer","Writer","Composer"],
            ["Actor","Director","Productor","Escritor","Compositor"]]

    for i in range(0,len(roles)):
        for j in range(0,len(roles[0])):
            params = urllib.parse.urlencode({
                'role': (j+1),
                'lang': (i+1),
                'name': roles[i][j]
            })
            c.request('POST', '/api/role_lang/', params, headers)
            #get the response back
            res = c.getresponse()
            print(res.status, res.reason)
            # at this point you could check the status etc
            # this gets the page text
            data = res.read()
            print(data)
