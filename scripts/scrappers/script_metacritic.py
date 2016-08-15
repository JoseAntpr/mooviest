import urllib.request, json
from bs4 import BeautifulSoup
from . import interface


# get_url_metacritic_by_imdb(imdb), return metacritic url by imdb
#
#   Params
#       - imdb, movie id of imdb
#
def get_url_metacritic_by_imdb(imdb):
    error_message = "IMDb id: " + str(imdb) + " - Script rating Metacritic\n"
    url = "http://www.imdb.com/title/"+imdb+"/criticreviews?ref_=tt_ov_rt"
    error_code = False

    error_code, msg, soup = interface.get_soup(url)
    if error_code:
        error_message += msg
        return error_code, error_message

    url_metacritic = ""
    try:
        lista = soup.find_all("div",{"class":"see-more"})
        if len(lista) > 0:
            url_metacritic = lista[0].find_all("a")[0].get('href')
        else:
            error_code = True
    except AttributeError:
        error_code = True

    if error_code:
        error_message += "Error get url of metacritic, imdb page\n"
        return error_code, error_message

    return error_code, error_message, url_metacritic

# format_params(rating, count), sourceid returns, rating formatted
#
#   Params
#       - rating, rating of Metacritic
#       - count, count of Metacritic
#
def format_params(rating, count):
    error_code = False
    error_message = ""
    try:
        count = count.replace("ratings","").strip()
        rating = int(rating.replace(".", "").replace(",", ""))
        count = int(count.replace(".", "").replace(",", ""))
    except:
        rating = 0
        count = 0
        error_code = True
        error_message = "Error format params \n"

    return error_code, error_message, rating, count



# get_rating(soup): sourceid returns, rating and count formatted
#
#   Params
#       - soup, soup Metacritic movie page
#
def get_rating(soup):
    error_code = False
    error_message = ""
    rating = ""
    count = ""
    try:
        lista = soup.find_all("div",{"class":"user"})
        if len(lista) > 0:
            rating = lista[0].get_text().strip()
            lista = soup.find_all("div",{"class":"details side_details"})
            lista = lista[0].find_all("span",{"class":"count"})
            count = lista[0].find("a").get_text().lower()
    except AttributeError:
        rating = ""
        count = ""
        error_code = True
        error_message = "Error get audience\n"
    if error_code:
        error_message += msg
        return error_code, error_message
    return format_params(rating, count)

# get_rating_expert(soup): sourceid returns, rating and count unformatted
#
#   Params
#       - soup, soup Metacritic movie page
#
def get_rating_expert(soup):
    error_code = False
    error_message = ""
    rating = ""
    count = ""
    try:
        lista = soup.find_all("div",{"class":"metascore_wrap highlight_metascore"})
        if len(lista) > 0:
            # print(lista)
            rating = lista[0].find_all("span",{"itemprop":"ratingValue"})[0].get_text().strip()
            count = lista[0].find_all("span",{"itemprop":"reviewCount"})[0].get_text().strip()
    except AttributeError:
        rating = ""
        count = ""
        error_code = True
        error_message = "Error get expert\n"
    if error_code:
        error_message += msg
        return error_code, error_message
    return format_params(rating, count)

def insert(db, movie_id, url, soup, expert):
    error_code = False
    error_message = ""
    rating = 0
    count = 0
    name = "Metacritic"
    if expert:
        error_code, error_message, rating, count = get_rating_expert(soup)
        name = "Metacritic Expert"
    else:
        error_code, error_message, rating, count = get_rating(soup)

    if error_code:
        error_message += msg
        return error_code, error_message

    params = json.dumps(
        {
            "source": db.SOURCES["Metacritic"],
            "movie": movie_id,
            "sourceid": url,
            "name": "Metacritic",
            "rating": rating,
            "count": count
        }
    )
    return error_code, error_message, db.insert_data(db.API_URLS["rating"], params)

def update(db, rating_id, soup, expert):
    error_code = False
    error_message = ""
    rating = 0
    count = 0

    if expert:
        error_code, error_message, rating, count = get_rating_expert(soup)
    else:
        error_code, error_message, rating, count = get_rating(soup)

    if error_code_expert:
        error_message += msg
        return error_code, error_message

    params = json.dumps(
        {
            "rating": rating,
            "count": count
        }
    )
    return error_code, error_message, db.update_data(db.API_URLS["rating"]+str(rating_id)+"/", params)

# insert_rating(db, movie_name, movie_id), insert rating, count and id movie
#                  of Metacritic
#   Params
#       - db, Object DB
#       - movie_id, id of the movie in mooviest db
#       - imdb, id movie of imdb
def insert_rating(db, movie_id, imdb):
    error_message = "Movie id: " + str(movie_id) + " - Script rating Metacritic\n"

    error_code, msg, url = get_url_metacritic_by_imdb(imdb)
    if error_code:
        error_message += msg
        return error_code, error_message


    error_code, msg, soup = interface.get_soup(url)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, res = insert(db, movie_id, url, soup, False)
    if error_code:
        error_message += msg

    error_code_expert, msg, res_expert = insert(db, movie_id, url, soup, True)
    if error_code_expert:
        error_message += msg

    return (error_code or error_code_expert), error_message, res, res_expert


# update_rating(db, movie_name, movie_id), update rating
#
#   Params
#       - db, Object DB
#       - rating_id, id of rating
#       - sourceid, url of Metacritic

def update_rating(db, rating_id, rating_expert_id, sourceid):
    error_message = "Rating id: " + str(rating_id) +", rating_expert id: " + str(rating_expert_id) +" - Script rating Metacritic\n"

    error_code, msg, soup = get_soup(sourceid)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, res = update(db, movie_id, url, soup, False)
    if error_code:
        error_message += msg

    error_code_expert, msg, res_expert = update(db, movie_id, url, soup, True)
    if error_code_expert:
        error_message += msg

    return (error_code or error_code_expert), error_message, res, res_expert
