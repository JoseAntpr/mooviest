import psycopg2, urllib.request, urllib.parse, http.client, json
from base64 import b64encode
from bs4 import BeautifulSoup
from . import interface

# format_params(sourceid, rating, count), sourceid returns, rating and count formatted
#
#   Params
#       - sourceid, id of FilmAffinity
#       - rating, rating of FilmAffinity
#       - count, count of FilmAffinity
#
def format_params(sourceid, rating, count):
    error_code = False
    error_message = ""
    try:
        sourceid = int(sourceid.replace("/es/film","").replace(".html",""))
        rating = int(rating.replace(",", ""))
        count = int(count.replace(".", ""))
    except:
        rating = 0
        count = 0
        sourceid = 0
        error_code = True
        error_message = "Error format params, rating FilmAffinity\n"

    return error_code, error_message, sourceid, rating, count

# get_rating_movie_page(soup): sourceid returns, rating and count unformatted
#
#   Params
#       - soup, soup FilmAffinity movie page
#
def get_rating_movie_page(soup):
    error_code = False
    error_message = ""
    rating = ""
    count = ""
    sourceid = ""
    try:
        rating = soup.find(id="movie-rat-avg").get_text().strip()
        count = soup.find(itemprop="ratingCount").get_text().strip()
        sourceid = soup.find_all("li",{"class":"active"})[0].find('a').get('href')
    except AttributeError:
        rating = 0
        count = 0
        sourceid = 0
        error_code = True
        error_message = "Error get audience, movie page, rating FilmAffinity\n"
    return error_code, error_message, sourceid, rating, count

# get_rating_search_page(soup, lista): sourceid returns, rating and count unformatted
#
#   Params
#       - soup, soup FilmAffinity movie page
#       - lista, list of movie found
#
def get_rating_search_page(soup, lista):
    error_code = False
    error_message = ""
    rating = ""
    count = ""
    sourceid = ""
    try:
        rating = lista[0].get_text().strip()
        lista = soup.find_all("div",{"class":"ratcount-box"})
        count = lista[0].get_text().strip()
        sourceid = soup.find_all("div",{"class":"mc-title"})[0]
        sourceid = sourceid.find_all("a")[0].get('href')
    except AttributeError:
        rating = 0
        count = 0
        sourceid = 0
        error_code = True
        error_message = "Error get audience, search page, rating FilmAffinity\n"
    return error_code, error_message, sourceid, rating, count

def get_rating(soup):
    lista = soup.find_all("div",{"class":"avgrat-box"})
    if len(lista) > 0:
        return get_rating_search_page(soup, lista)
    else:
        return get_rating_movie_page(soup)


# insert_rating(db, movie_name, movie_id), insert rating, count and id movie
#                  of FilmAffinitty, with name(in spanish) movie_name
#   Params
#       - db, Object DB
#       - movie_name, name(in spanish) of the movie
#       - movie_id, id of the movie in mooviest db
def insert_rating(db, movie_id, movie_name):
    search = urllib.parse.quote_plus(movie_name)
    url = "http://www.filmaffinity.com/es/search.php?stext="+search+"&stype=all"
    error_message = ""

    error_code, msg, soup = interface.get_soup(url)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, sourceid, rating, count = get_rating(soup)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, sourceid, rating, count = format_params(sourceid, rating, count)
    error_message += msg
    res = {}
    if  not error_code:
        params = json.dumps(
            {
                "source": db.SOURCES["FilmAffinity"],
                "movie": movie_id,
                "sourceid": sourceid,
                "name": "FilmAffinity",
                "rating": rating,
                "count": count
            }
        )
        try:
            res = db.insert_data(db.API_URLS["rating"], params)
        except:
            error_message += "Error insert rating FilmAffinity\n"
            error_code = True


    return error_code, error_message, res

# update_rating(db, movie_name, movie_id), update rating
#
#   Params
#       - db, Object DB
#       - rating_id, id of rating
#       - sourceid, id of FilmAffinity

def update_rating(db, rating_id, sourceid):
    error_message = "Rating id: " + str(rating_id) + " - Script rating FilmAffinity\n"
    url = "https://www.filmaffinity.com/es/film"+str(sourceid)+".html"

    error_code, msg, soup = interface.get_soup(url)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, sourceid, rating, count = get_rating_movie_page(soup)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, sourceid, rating, count = format_params(sourceid, rating, count)
    error_message += msg
    res = {}
    if not error_code:
        params = json.dumps(
            {
                "rating": rating,
                "count": count
            }
        )
        try:
            res = db.update_data(db.API_URLS["rating"]+str(rating_id)+"/", params)
        except:
            error_message += "Error update rating\n"
            error_code = True

    return error_code, error_message, res
