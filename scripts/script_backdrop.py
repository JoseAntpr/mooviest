import psycopg2, urllib.request, urllib.parse, http.client, json, time
from base64 import b64encode

import interface
import interface_db
from script_tviso import interface as interface_tviso


db = interface_db.DB("admin","admin")

api_url = "/api/movie_app_bylang?lang_id=2&limit=200000"
caracter_delete = "EXTERNAL#"


def get_info_tviso(idm, auth_token):
    mediaType = "2"
    url = "https://api.tviso.com/media/"+mediaType+"-"+idm+"/XX/release?auth_token=" + auth_token
    error_message = ""
    data = {}

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf8"))
        error = data["error"]
    except:
	    error_message = "Error call get_info_tviso url: " + url + "\n"
	    error = 2
    if error == 1:
        error_message = "error: Auth token\n"
        auth_token = interface_tviso.get_token()
    elif(error == 9 or error == 50):
	    error_message = "error: Media type\n"

    elif error == 10:
	    error_message = "error: Idm\n"

    elif error == 20:
        error_message = "error: Quota exceeded\n"

    elif error == 502:
	    error_message = "error: Response timeout or internet connection is not available\n"

    elif error == 803:
	    error_message = "error: Media limit reached\n"

    return error, error_message, auth_token, data


def external_image(movie_id, movie_lang_id, idm, image,auth_token):
    #update Movie_lang
    image.replace(caracter_delete,"")
    #update movie backdrop and get tviso
    # print(auth_token)
    error_code, error_message, auth_token, data = get_info_tviso(idm, auth_token)
    while error_code == 1:
        error_code, error_message, auth_token, data = get_info_tviso(idm, auth_token)
    # print(data)
    backdrop = str(data["media"]["images"]["backdrop"])
    if error_code == 0:
        db.update_data(db.API_URLS["movie"]+movie_id+"/",json.dumps({"backdrop": backdrop}))
        db.update_data(db.API_URLS["movie_lang"]+movie_lang_id+"/",json.dumps({"image": image}))
    else:
        interface.save_log(interface.log_txt, "Movie idm: "+idm+"\n Mooviest id: "+movie_id+"\n" + error_message + "\n")


def insert_update_backdrop(api_url,auth_token):
    response = db.search(api_url)
    next_url = str(response["next"])
    count = str(response["count"])
    movies = response["results"]

    for movie in movies:
        image = str(movie["langs"][0]["image"])
        movie_id = str(movie["id"])
        if image.find(caracter_delete) < 0:
            db.update_data(db.API_URLS["movie"]+movie_id+"/",json.dumps({"backdrop": image}))
        else:
            movie_lang_id = str(movie["langs"][0]["id"])
            idm = str(movie["ratings"][0]["sourceid"])
            external_image(movie_id, movie_lang_id, idm, image,auth_token)
    return next_url, count

# Generate token
auth_token = interface_tviso.get_token()

next_url, count = insert_update_backdrop(api_url,auth_token)
i = 0
print(str(i)+"/"+count)
while next_url != None:
    next_url, count = insert_update_backdrop(api_url,auth_token)
    i += 1
    print(str(i)+"/"+count)

# next_url = str(result["next"])
# results


# while next_url != None:


# print(next_url)
# print(str(result["previous"]))
