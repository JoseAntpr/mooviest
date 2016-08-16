import urllib.request, json
from bs4 import BeautifulSoup
from . import interface

# get_url_rottentomatoes_by_omdb(id_imdb), return rottentomatoes url by omdb
#   Params
#       - id_imdb, movie id of imdb
def get_url_rottentomatoes_by_omdb(id_imdb):
    url = "http://www.omdbapi.com/?i=" + id_imdb + "&tomatoes=true&plot=full&r=json"
    url_rotten = ""
    error_code = False
    error_message = ""

    try:
        response = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = json.loads(urllib.request.urlopen(response).read().decode("utf8"))
        url_rotten = data["tomatoURL"]

        url_rotten = str(url_rotten.replace("http", "")
        .replace("https", "").replace("://www.rottentomatoes.com/m/","")
        .replace("/",""))
    except:
        error_code = True
        error_message = "Error to get url of rottentomatoes, OMDB API"

    return error_code, error_message, url_rotten


# get_expert_rating(soup), get expert rating of Rotten Tomatoes,
#   Params
#       - soup, page from BeautifulSoup
def get_expert_rating(soup):

    # TOMATOMETER - RottenTomatoesExpert
    # Div with RottenTomatoesExpert
    lista = soup.find_all("div", {"class":"tomato-left"}, {"class":"critic-score meter"})[0]
    # Rating
    rating = lista.find("span","meter-value").find("span").get_text()
    # Count
    count = lista.find(id="scoreStats").find_all("div","superPageFontColor")[1].find_all("span")[1].get_text()

    return rating, count

# get_audience_rating(soup), get audience rating of Rotten Tomatoes,
#   Params
#       - soup, page from BeautifulSoup
def get_audience_rating(soup):

    # AUDIENCE SCORE - RottenTomatoesAudience
    # Div with RottenTomatoesAudience
    lista = soup.find_all("div", {"class":"audiencepanel"})[0]
    # Rating
    rating = lista.find_all("div", {"class":"audience-score meter"})[0].find("span","superPageFontColor").get_text()
    rating = int(rating.replace("%", ""))
    # Count
    count = lista.find("div","audience-info").find_all("div")[1].get_text()
    count = int(count.replace("User Ratings:", "").strip().replace(",",""))

    return rating, count

# insert_expert(soup, movie_id, sourceid, db, error_code), insert expert rating
#                                          of Rotten Tomatoes,
#   Params
#       - soup, page from BeautifulSoup
#       - movie_id, id of the movie in mooviest db
#       - sourceid, sourceid from mooviest db
#       - db, interface db
#       - error_code, error propagated
def insert_expert(soup, movie_id, sourceid, db, error_code):

    res_expert = {}
    error_message = ""

    try:
        rating, count = get_expert_rating(soup)
        params = json.dumps(
            {
                "source": db.SOURCES["RottenTomatoes"],
                "movie": movie_id,
                "sourceid": sourceid,
                "name": "RottenTomatoesExpert",
                "rating": rating,
                "count": count
            }
        )
        res_expert = db.insert_data(db.API_URLS["rating"], params)
        error_message = "Insert expert rating successfully\n"

    except:
        error_message = "Error insert expert rating\n"
        error_code = True

    return error_code, error_message, res_expert


# insert_audience(soup, movie_id, sourceid, db, error_code), insert audience rating
#                                          of Rotten Tomatoes,
#   Params
#       - soup, page from BeautifulSoup
#       - movie_id, id of the movie in mooviest db
#       - sourceid, sourceid from mooviest db
#       - db, interface db
#       - error_code, error propagated
def insert_audience(soup, movie_id, sourceid, db, error_code):

    res_audience = {}
    error_message = ""

    try:
        rating, count = get_audience_rating(soup)
        params = json.dumps(
            {
                "source": db.SOURCES["RottenTomatoes"],
                "movie": movie_id,
                "sourceid": sourceid,
                "name": "RottenTomatoesAudience",
                "rating": rating,
                "count": count
            }
        )
        res_audience = db.insert_data(db.API_URLS["rating"], params)
        error_message = "Insert audience rating successfully\n"

    except:
        error_message += "Error insert audience rating\n"
        error_code = True

    return error_code, error_message, res_audience

# update_expert(soup, rating_id, db, error_code), update expert rating
#                                          of Rotten Tomatoes,
#   Params
#       - soup, page from BeautifulSoup
#       - rating_id, rating id to update
#       - db, interface db
#       - error_code, error propagated
def update_expert(soup, rating_id, db, error_code):

    res_expert = {}
    error_message = ""

    try:
        rating, count = get_expert_rating(soup)
        params = json.dumps(
            {
                "rating": rating,
                "count": count
            }
        )
        res_expert = db.update_data(db.API_URLS["rating"] + str(rating_id) + "/", params)
        error_message = "Update expert rating successfully\n"

    except:
        error_message = "Error update expert rating\n"
        error_code = True

    return error_code, error_message, res_expert

# update_audience(soup, rating_id, db, error_code), update audience rating
#                                          of Rotten Tomatoes,
#   Params
#       - soup, page from BeautifulSoup
#       - rating_id, rating id to update
#       - db, interface db
#       - error_code, error propagated
def update_audience(soup, rating_id, db, error_code):

    res_audience = {}
    error_message = ""

    try:
        rating, count = get_audience_rating(soup)
        params = json.dumps(
            {
                "rating": rating,
                "count": count
            }
        )
        res_audience = db.update_data(db.API_URLS["rating"] + str(rating_id) + "/", params)
        error_message = "Update audience rating successfully\n"

    except:
        error_message = "Error update audience rating\n"
        error_code = True

    return error_code, error_message, res_audience


# insert_rating(db, movie_id, sourceid), insert expert and audience rating
#                                          of Rotten Tomatoes,
#   Params
#       - db, interface db
#       - movie_id, id of the movie in mooviest db
#       - sourceid, sourceid for make the url of Rotten Tomatoes
def insert_rating(db, movie_id, sourceid):

    url = "https://www.rottentomatoes.com/m/" + sourceid + "/"
    error_message = "Movie id: " + str(movie_id) + " - Script INSERT rating Rotten Tomatoes\n URL:" + url + "\n"
    res_expert = {}
    res_audience = {}

    # Get soup from url
    error_code, msg, soup = interface.get_soup(url)

    if not error_code:
        # Insert expert rating
        error_code, msg, res_expert = insert_expert(soup, movie_id, sourceid, db, error_code)
        error_message += msg

        # Insert audience rating
        error_code, msg, res_audience = insert_audience(soup, movie_id, sourceid, db, error_code)
        error_message += msg

    else:
        error_message += msg

    return error_code, error_message, res_expert, res_audience

# update_rating(db, rating_expert_id, rating_audience_id, sourceid),
#             update expert and audience rating of Rotten Tomatoes,
#   Params
#       - db, interface db
#       - rating_audience_id, rating audience id
#       - rating_expert_id, rating expert id
#       - sourceid, sourceid for make the url of Rotten Tomatoes
def update_rating(db, rating_audience_id, rating_expert_id, sourceid):

    url = "https://www.rottentomatoes.com/m/" + sourceid + "/"
    error_message = "Rating audience id: " + str(rating_audience_id) + " Rating expert id: " + str(rating_expert_id) + " - Script UPDATE rating Rotten Tomatoes\n URL:" + url + "\n"
    res_expert = {}
    res_audience = {}

    # Get soup from url
    error_code, msg, soup = interface.get_soup(url)

    if not error_code:
        # Update expert rating
        error_code, msg, res_expert = update_expert(soup, rating_expert_id, db, error_code)
        error_message += msg

        # Update audience rating
        error_code, msg, res_audience = update_audience(soup, rating_audience_id, db, error_code)
        error_message += msg

    else:
        error_message += msg

    return error_code, error_message, res_expert, res_audience
