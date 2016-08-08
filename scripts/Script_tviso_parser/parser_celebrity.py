import json

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
        celebrity = {
                "name": name,
                "born": None,
                "image": image,
                "twitter_account": ""
            }
        celebrity_list.append(json.dumps(celebrity))
    #Compose
    for celeb in data["compose"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        name = celeb["name"]
        celebrity = {
                "name": name,
                "born": None,
                "image": image,
                "twitter_account": ""
            }
        celebrity_list.append(json.dumps(celebrity))
    #Director
    for celeb in data["director"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        name = celeb["name"]
        celebrity = {
                "name": name,
                "born": None,
                "image": image,
                "twitter_account": ""
            }
        celebrity_list.append(json.dumps(celebrity))
    #Write
    for celeb in data["write"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        name = celeb["name"]
        celebrity = {
                "name": name,
                "born": None,
                "image": image,
                "twitter_account": ""
            }
        celebrity_list.append(json.dumps(celebrity))

    return celebrity_list
