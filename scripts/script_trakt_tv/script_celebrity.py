from . import interface

def get_info_celebrity(name):
    person = name.replace(" ","-").lower()
    url_person = "/people/" + person + "?extended=full"
    print(name)
    print(url_person)
    data = interface.get_info(url_person)

    born = data["birthday"]
    address = data["birthplace"]
    biography = data["biography"]

    return born, address, biography
