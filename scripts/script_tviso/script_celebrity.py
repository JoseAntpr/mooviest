import json

def get_celebrities(data):
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
                "born": "0001-01-01",
                "image": image,
                "twitter_account": "",
                "address": ""
            }
        celebrity_list.append(celebrity)
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
                "born": "0001-01-01",
                "image": image,
                "twitter_account": "",
                "address": ""
            }
        celebrity_list.append(celebrity)
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
                "born": "0001-01-01",
                "image": image,
                "twitter_account": "",
                "address": ""
            }
        celebrity_list.append(celebrity)
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
                "born": "0001-01-01",
                "image": image,
                "twitter_account": "",
                "address": ""
            }
        celebrity_list.append(celebrity)

    return celebrity_list
