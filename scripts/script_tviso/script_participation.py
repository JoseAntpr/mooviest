import json
from . import interface

def get_participations(data, movie_id):
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
                "celebrity": 0,
                "movie": movie_id,
                "role": interface.ROLES["actor"],
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
                "celebrity": 0,
                "movie": movie_id,
                "role": interface.ROLES["composer"],
                "character": "_",
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
                "celebrity": 0,
                "movie": movie_id,
                "role": interface.ROLES["director"],
                "character": "_",
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
                "celebrity": 0,
                "movie": movie_id,
                "role": interface.ROLES["writer"],
                "character": "_",
                "award": ""
            }
        participation_list.append(json.dumps(participation))

    return participation_list
