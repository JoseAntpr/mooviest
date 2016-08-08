import psycopg2, urllib.request, json

def parser_celebrity(data):
    celebrity_list = []
    #Cast
    for celeb in data["cast"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        name = celeb["name"]
        celebrity = json.dumps(
                {
                    "name": name,
                    "born": None,
                    "image": image,
                    "twitter_account": ""
                }
            )
        celebrity_list.append(celebrity)
    #Compose
    for celeb in data["compose"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        name = celeb["name"]
        celebrity = json.dumps(
                {
                    "name": name,
                    "born": None,
                    "image": image,
                    "twitter_account": ""
                }
            )
        celebrity_list.append(celebrity)
    #Director
    for celeb in data["write"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        name = celeb["name"]
        celebrity = json.dumps(
                {
                    "name": name,
                    "born": None,
                    "image": image,
                    "twitter_account": ""
                }
            )
        celebrity_list.append(celebrity)

    return celebrity_list
