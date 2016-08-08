import json
import script_interface as interface

roles = {"actor":1 ,"director":2 ,"producer":3 ,"writer":4 ,"composer":5}


def parser_participation(data, celebrity_id, movie_id):
    participation_list = []
    #Cast
    for celeb in data["cast"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        character = celeb["role"]
        participation = {
                "celebrity": celebrity_id,
                "movie": movie_id,
                "role": roles["actor"],
                "character": character,
                "award": ""
            }
        participation_list.append(json.dumps(participation))
    #Compose
    for celeb in data["compose"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        name = celeb["name"]
        participation = {
                "celebrity": null,
                "movie": null,
                "role": roles["composer"],
                "character": "",
                "award": ""
            }
        participation_list.append(json.dumps(participation))
    #Director
    for celeb in data["director"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        name = celeb["name"]
        participation = {
                "celebrity": null,
                "movie": null,
                "role": roles["director"],
                "character": "",
                "award": ""
            }
        participation_list.append(json.dumps(participation))
    #Write
    for celeb in data["write"]:
        image = ""
        try:
            image =  celeb["images"]["face"]
        except TypeError:
            image = ""

        name = celeb["name"]
        participation = {
                "celebrity": null,
                "movie": null,
                "role": roles["writer"],
                "character": "",
                "award": ""
            }
        participation_list.append(json.dumps(participation))

    return participation_list

print(interface.langs["es"])
