import psycopg2, urllib.request, json

# get_info_tviso, return data format json, of the media with idm
#   Params
#       - idm, id(Tviso) of the media
#       - token, token of the API Tviso, generate with the data mooviest
#       - mediaType, type of media, 1-Serie/2-Movie/3-TvShow/4-Docu/5-Capitulo
#   if all ok, data["error"] == 0
def get_info_tviso(idm,token,mediaType):
    url = "https://api.tviso.com/media/full_info?auth_token=" + auth_token + "&idm=" + idm  + "&mediaType=" + mediaType
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode("utf8"))

    error = data["error"]

    if error == 1:
    	print('error: Auth token')
    elif(error == 9 or error == 50):
    	print(idm+' - error: Media type')
    elif error == 10:
    	print(idm+' - error: Idm')
    elif error == 20:
    	print(idm+' - error: Quota exceeded')
    elif error == 803:
        print("error: Media limit reached at number" + idm )
    else:
        print("All ok!")

    return data

def movie_parser_tviso(data):
    # MOVIE
    runtime = int(data["runtime"])
    released = int(data["year"])
    imdb = data["imdb"]
    movie_producer_list = []
    genre_list = []


    for produce in data["produce"]:
        movie_producer_list.append(produce["name"])

    producer = ' | '.join(movie_producer_list)

    for genre in data["genres"]:
        genre_list.append(genre)

    casting_list = []
    for actor in data["cast"]:
        face = ""
        try:
            face =  actor["images"]["face"]
            print(face)
        except TypeError:
            face = ""

        item = {
            "name": actor["name"],
            "name_film": actor["role"],
            "face": face
        }
        casting_list.append(item)
    print(casting_list)

    #return imdb, runtime, released, producer, genre_list

def movie_lang_parser_tviso(data):
    # MOVIE LANG
    title = str(data["name"])

    director_list = []
    for director in data["director"]:
    	director_list.append(director["name"])



    plot = str(data["plot"])

    return title, plot, director_list

id_api = '3504'
secret = 'bhRNt7TaHhuVcKxExK3n'
#auth_token = json.loads(urllib.request.urlopen('https://api.tviso.com/auth_token?id_api=' + id_api + '&secret=' + secret).read().decode('utf8'))["auth_token"]
auth_token = "85fe8eceed84c250d254be5aed2ba525"
print(auth_token)
mediaType = "2"
idm = "10"
data = get_info_tviso(idm,auth_token,mediaType)
print(data["error"])
#print(data)
movie_parser_tviso(data)
