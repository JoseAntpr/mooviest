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
    try:
        casts = data["cast"]
    except:
        casts = []
    for celeb in casts:
        celebrity = get_celebrity(celeb)
        celebrity_list.append(celebrity)
        participation = get_participation(movie_id, celeb, interface.ROLES["actor"])
        participation_list.append(participation)
    #Compose
    try:
        casts = data["compose"]
    except:
        casts = []
    for celeb in casts:
        celebrity = get_celebrity(celeb)
        celebrity_list.append(celebrity)
        participation = get_participation(movie_id, celeb, interface.ROLES["composer"])
        participation_list.append(participation)
    #Director
    try:
        casts = data["director"]
    except:
        casts = []
    for celeb in casts:
        celebrity = celebrity = get_celebrity(celeb)
        celebrity_list.append(celebrity)
        participation = get_participation(movie_id, celeb, interface.ROLES["director"])
        participation_list.append(participation)
    #Write
    try:
        casts = data["write"]
    except:
        casts = []
    for celeb in casts:
        celebrity = get_celebrity(celeb)
        celebrity_list.append(celebrity)
        participation = get_participation(movie_id, celeb, interface.ROLES["writer"])
        participation_list.append(participation)

    return celebrity_list, participation_list
