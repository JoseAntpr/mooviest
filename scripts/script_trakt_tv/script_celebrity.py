import json
from . import interface as inter

def get_info_celebrity(name):
    person = inter.strip_accents(name)
    person = person.replace(".","-").replace(" ","-").replace("--","-").replace("'","-").lower()
    if person[len(person)-1] == "-":
        person = person[:-1]
    url_person = "/people/" + person + "?extended=full"
    error_code = False
    error_message = ""
    born = None
    address = ""
    biography = ""
    try:
        data = inter.get_info(url_person)
        born = data["birthday"]
        address = data["birthplace"]
        biography = data["biography"]
    except:
        born = None
        address = ""
        biography = ""
        error_message = "Error info celebrity trakt.tv "+ name +" "+person+"\n"
        error_code = True

    return error_code, error_message, born, address, biography
