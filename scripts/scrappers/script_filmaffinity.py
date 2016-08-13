import psycopg2, urllib.request, urllib.parse, http.client, json
from base64 import b64encode
from bs4 import BeautifulSoup

def get_soup(url):
    error_code = False
    error_message = ""
    soup = ""
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode("utf8")
        soup = BeautifulSoup(html, 'html.parser')
    except AttributeError:
        error_code = True
        error_message = "Error call \n"
        soup = ""
    return error_code, error_message, soup

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
        error_message = "Error format params \n"

    return error_code, error_message, sourceid, rating, count

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
        error_message = "Error get audience, movie page \n"
    return error_code, error_message, sourceid, rating, count

def get_rating_search_page(soup,lista):
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
        error_message = "Error get audience, search page \n"
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
    error_message = "Movie id: " + str(movie_id) + " - Script rating FilmAffinity\n url:"+url+"\n"

    error_code, msg, soup = get_soup(url)
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

        res = db.insert_data(db.API_URLS["rating"], params)

    return error_code, error_message, res

# update_rating(db, movie_name, movie_id), update rating
#
#   Params
#       - db, Object DB
#       - rating, record to update

def update_rating(db, rating):
    error_message = "Movie id: " + str(rating["movie"]) + " - Script rating Rotten Tomatoes\n"
    url = "https://www.filmaffinity.com/es/film"+rating["sourceid"]+".html"

    error_code, msg, soup = get_soup(url)
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
        rating["rating"] = rating
        rating["count"] = count
        res = db.update(db.API_URLS["rating"], count)

    return error_code, error_message, res
