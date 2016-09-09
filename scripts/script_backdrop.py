import psycopg2, urllib.request, urllib.parse, http.client, json, time
from base64 import b64encode

import interface
import interface_db
from script_tviso import interface as interface_tviso


db = interface_db.DB("admin","admin")

api_url = "/api/movie_app_bylang?idlang_id=2&limit=200000"
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

    if error_code == 0:
        try:
            backdrop = data["media"]["images"]["backdrop"]
            backdrop.replace(caracter_delete,"")
            db.update_data(db.API_URLS["movie"]+movie_id+"/",json.dumps({"backdrop": backdrop}))
            db.update_data(db.API_URLS["movie_lang"]+movie_lang_id+"/",json.dumps({"image": image}))
        except:
            log = "\nMovie idm: "+idm+"\n Mooviest id: "+movie_id+"\n Error data: "+str(data)+"\n"
            print(log)
            interface.save_log(interface.log_txt, log)
            backdrop = ""
            db.update_data(db.API_URLS["movie"]+movie_id+"/",json.dumps({"backdrop": backdrop}))
    else:
        log = "\nMovie idm: "+idm+"\n Mooviest id: "+movie_id+"\n" + error_message+"\n"
        print(log)
        interface.save_log(interface.log_txt, log)


def insert_update_backdrop(movie_id,auth_token):
    error_code = False
    api_url = "/api/movie_app_bylang?id="+str(movie_id)+"&lang_id=2"
    response = db.search(api_url)
    try:
        movies = response["results"]
    except:
        log = "\nMooviest id: "+movie_id+" no existe la movie\n"
        print(log)
        interface.save_log(interface.log_txt, log)
        movies = []
        error_code = True

    if not error_code:
        for movie in movies:
            movie_id = str(movie["id"])
            try:
                image = str(movie["langs"][0]["image"])
            except:
                log = "\nMooviest id: "+movie_id+" no tiene image\n"
                print(log)
                interface.save_log(interface.log_txt, log)
                error_code = True
            if not error_code:
                if image.find(caracter_delete) < 0:
                    db.update_data(db.API_URLS["movie"]+movie_id+"/",json.dumps({"backdrop": image}))
                else:
                    try:
                        movie_lang_id = str(movie["langs"][0]["id"])
                        idm = str(movie["ratings"][0]["sourceid"])
                        external_image(movie_id, movie_lang_id, idm, image,auth_token)
                    except:
                        log = "\nMooviest id: "+movie_id+" no tiene sourceid\n"
                        print(log)
                        interface.save_log(interface.log_txt, log)

# Generate token
auth_token = interface_tviso.get_token()

for i in range(1, 181874):
    insert_update_backdrop(i,auth_token)
    print(str(i)+"/181874")
