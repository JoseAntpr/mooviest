import urllib.request, json
from bs4 import BeautifulSoup

# get_soup(url), return soup
#
#   Params
#       - url, url that will scrapper
#
def get_soup(url):
    error_code = False
    error_message = ""
    soup = ""
    try:
        response = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html =  urllib.request.urlopen(response).read().decode("utf8")
        soup = BeautifulSoup(html, 'html.parser')
    except AttributeError:
        error_code = True
        error_message = "Error call \n"
        soup = ""
    return error_code, error_message, soup

# get_url_metacritic_by_imdb(imdb), return metacritic url by imdb
#
#   Params
#       - imdb, movie id of imdb
#
def get_url_metacritic_by_imdb(imdb):
    error_message = "IMDb id: " + str(imdb) + " - Script rating Metacritic\n"
    url = "http://www.imdb.com/title/"+imdb+"/criticreviews?ref_=tt_ov_rt"
    error_code = False

    error_code, msg, soup = get_soup(url)
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
        rating = int(rating.replace(".", "").replace(",", ""))
        count = int(count.replace(".", "").replace(",", ""))
    except:
        rating = 0
        count = 0
        error_code = True
        error_message = "Error format params \n"

    return error_code, error_message, rating, count



# get_rating(soup): sourceid returns, rating and count unformatted
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
            count = count.replace("ratings","").strip()
    except AttributeError:
        rating = ""
        count = ""
        error_code = True
        error_message = "Error get audience\n"
    return error_code, error_message, rating, count


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

    error_code, msg, soup = get_soup(url)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, rating, count = get_rating(soup)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, rating, count = format_params(rating, count)
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
    return db.insert_data(db.API_URLS["rating"], params)

# update_rating(db, movie_name, movie_id), update rating
#
#   Params
#       - db, Object DB
#       - rating_id, id of rating
#       - sourceid, url of Metacritic

def update_rating(db, rating_id, sourceid):
    error_message = "Rating id: " + str(rating_id) + " - Script rating Metacritic\n"

    error_code, msg, soup = get_soup(sourceid)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, rating, count = get_rating(soup)
    if error_code:
        error_message += msg
        return error_code, error_message

    error_code, msg, rating, count = format_params(rating, count)
    if error_code:
        error_message += msg
        return error_code, error_message

    res = {}
    if not error_code:
        params = json.dumps(
            {
                "rating": rating,
                "count": count
            }
        )
        res = db.update_data(db.API_URLS["rating"]+str(rating_id)+"/", params)

    return error_code, error_message, res
