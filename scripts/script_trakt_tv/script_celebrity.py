from . import interface

def get_info_celebrity(name):
    person = name.replace(".","-").replace(" ","-").replace("--","-").lower()
    url_person = "/people/" + person + "?extended=full"
    error_code = False
    error_message = ""
    born = None
    address = ""
    biography = ""
    try:
        data = interface.get_info(url_person)
        born = data["birthday"]
        address = data["birthplace"]
        biography = data["biography"]
    except:
        born = None
        address = ""
        biography = ""
        error_message = "Error info celebrity trakt.tv "+ name + "\n"
        error_code = True

    return error_code, error_message, born, address, biography
