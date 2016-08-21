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
        sourceid = int(sourceid.replace("/en/film","").replace(".html",""))
        rating = int(rating.replace(".", "").replace(",", ""))
        count = int(count.replace(",", "").replace(".", ""))
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
    rating = 0
    count = 0
    sourceid = 0
    try:
        rating = soup.find(id="movie-rat-avg").get_text().strip()
        error_message = rating
        count = soup.find(itemprop="ratingCount").get_text().strip()
        sourceid = soup.find_all("li",{"class":"active"})[0].find('a').get('href')
    except:
        error_code = True
        error_message += "Error get audience, movie page, rating FilmAffinity soup\n"
    return error_code, error_message, sourceid, rating, count

def get_search_released(soup, released):
    lista = soup.find_all("div", {"class":"se-it"})
    year = 0
    found = False
    i = 0
    while i < len(lista) and not found:
        year_str = lista[i].find("div",{"class":"ye-w"}).get_text()
        if year_str != "":
            year = int(year_str)
        if year == released:
            soup = lista[i]
            found = True
        i += 1
    return found, soup
# get_rating_search_page(soup, lista): sourceid returns, rating and count unformatted
#
#   Params
#       - soup, soup FilmAffinity movie page
#       - lista, list of movie found
#
def get_rating_search_page(soup, lista, released):
    error_code = False
    error_message = ""
    rating = 0
    count = 0
    sourceid = 0
    try:
        found, soup = get_search_released(soup, released)
        print(found)
        if found:
            rating = soup.find("div",{"class":"avgrat-box"}).get_text()
            count = soup.find("div",{"class":"ratcount-box"}).get_text()
            sourceid = soup.find("div",{"class":"mc-title"}).find("a").get('href')
        else:
            print("Entra")
            error_code = True
            error_message = "Error get audience, search page, rating FilmAffinity by released\n"
    except:
        error_code = True
        error_message = "Error get audience, search page, rating FilmAffinity\n"
    print(error_message)
    return error_code, error_message, sourceid, rating, count

def get_rating(soup, released):
    lista = soup.find_all("div",{"class":"avgrat-box"})
    if len(lista) > 0:
        return get_rating_search_page(soup, lista, released)
    else:
        return get_rating_movie_page(soup)


# insert_rating(db, movie_name, movie_id), insert rating, count and id movie
#                  of FilmAffinitty, with name(in spanish) movie_name
#   Params
#       - db, Object DB
#       - movie_name, name(in spanish) of the movie
#       - movie_id, id of the movie in mooviest db
def insert_rating(db, movie_id, movie_name, released):
    search = urllib.parse.quote_plus(movie_name)
    url = "http://www.filmaffinity.com/en/search.php?stext="+search+"&stype=all"
    error_message = ""
    res = {}
    error_code, msg, soup = interface.get_soup(url)
    if error_code:
        error_message += msg
        return error_code, error_message, res

    error_code, msg, sourceid, rating, count = get_rating(soup, released)

    if error_code:
        error_message += msg
        return error_code, error_message, res

    error_code, msg, sourceid, rating, count = format_params(sourceid, rating, count)
    error_message += msg

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
    res = {}

    error_code, msg, soup = interface.get_soup(url)
    if error_code:
        error_message += msg
        return error_code, error_message, res

    error_code, msg, sourceid, rating, count = get_rating_movie_page(soup)
    if error_code:
        error_message += msg
        return error_code, error_message, res

    error_code, msg, sourceid, rating, count = format_params(sourceid, rating, count)
    error_message += msg

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
