import json
#import ..scripts as interface

# import psycopg2, urllib.request, urllib.parse, http.client, json
# from base64 import b64encode
#
#
# def get_info_tviso(idm,token,mediaType):
#     url = "https://api.tviso.com/media/full_info?auth_token=" + auth_token + "&idm=" + idm  + "&mediaType=" + mediaType
#     response = urllib.request.urlopen(url)
#     data = json.loads(response.read().decode("utf8"))
#
#     error = data["error"]
#
#     if error == 1:
#     	print('error: Auth token')
#     elif(error == 9 or error == 50):
#     	print(idm+' - error: Media type')
#     elif error == 10:
#     	print(idm+' - error: Idm')
#     elif error == 20:
#     	print(idm+' - error: Quota exceeded')
#     elif error == 803:
#         print("error: Media limit reached at number" + idm )
#     else:
#         print("All ok!")
#
#     return data

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
                "celebrity": celebrity_id,
                "movie": movie_id,
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
                "celebrity": celebrity_id,
                "movie": movie_id,
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
                "celebrity": celebrity_id,
                "movie": movie_id,
                "role": roles["writer"],
                "character": "",
                "award": ""
            }
        participation_list.append(json.dumps(participation))

    return participation_list

#print(interface.langs["es"])


# auth_token = "501504992d210df7c3034ef8a7089c67"
# mediaType = "2"
# idm = "5411"
# data = get_info_tviso(idm,auth_token,mediaType)
# datamovie = parser_participation(data, 1, 2)
# print(datamovie)
