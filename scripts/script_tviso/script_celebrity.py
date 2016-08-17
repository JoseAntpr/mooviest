import json
from . import interface

def get_celebrity(celeb):
    image = ""
    try:
        image =  celeb["images"]["face"]
    except:
        image = ""

    name = celeb["name"]
    celebrity = {
            "name": name,
            "born": None,
            "image": image,
            "twitter_account": "",
            "address": ""
        }

    return celebrity

def get_participation(movie_id, celeb, role ):
    character = ""
    try:
        character =  celeb["role"]
    except:
        character = ""
    participation = {
            "celebrity": 0,
            "movie": movie_id,
            "role": role,
            "character": character,
            "award": ""
        }

    return participation

def get_celebrities_and_participations(data, movie_id):
    celebrity_list = []
    participation_list = []
    #Cast
    for celeb in data["cast"]:
        celebrity = get_celebrity(celeb)
        celebrity_list.append(celebrity)
        participation = get_participation(movie_id, celeb, interface.ROLES["actor"])
        participation_list.append(participation)
    #Compose
    for celeb in data["compose"]:
        celebrity = get_celebrity(celeb)
        celebrity_list.append(celebrity)
        participation = get_participation(movie_id, celeb, interface.ROLES["composer"])
        participation_list.append(participation)
    #Director
    for celeb in data["director"]:
        celebrity = celebrity = get_celebrity(celeb)
        celebrity_list.append(celebrity)
        participation = get_participation(movie_id, celeb, interface.ROLES["director"])
        participation_list.append(participation)
    #Write
    for celeb in data["write"]:
        celebrity = get_celebrity(celeb)
        celebrity_list.append(celebrity)
        participation = get_participation(movie_id, celeb, interface.ROLES["writer"])
        participation_list.append(participation)

    return celebrity_list, participation_list
