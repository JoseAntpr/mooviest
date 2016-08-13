import urllib.request, urllib.parse, http.client, json
from base64 import b64encode
from bs4 import BeautifulSoup

# get_url_rottentomatoes_by_omdb(id_imdb), return rottentomatoes url by omdb
#
#   Params
#       - id_imdb, movie id of imdb
def get_url_rottentomatoes_by_omdb(id_imdb):
    url = "http://www.omdbapi.com/?i=" + id_imdb + "&tomatoes=true&plot=full&r=json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode("utf8"))
    url_rotten = data["tomatoURL"]

    url_rotten = str(url_rotten.replace("http://www.rottentomatoes.com/m/", "").replace("/",""))

    return url_rotten


# insert_expert(soup, movie_id, sourceid, db), insert expert rating
#                                          of Rotten Tomatoes,
#   Params
#       - soup, page from BeautifulSoup
#       - movie_id, id of the movie in mooviest db
#       - sourceid, sourceid from mooviest db
#       - db, interface db
def insert_expert(soup, movie_id, sourceid, db):

    # TOMATOMETER - RottenTomatoesExpert
    # Div with RottenTomatoesExpert
    lista = soup.find_all("div", {"class":"tomato-left"}, {"class":"critic-score meter"})[0]
    # Rating
    rating = lista.find("span","meter-value").find("span").get_text()
    # Count
    count = lista.find(id="scoreStats").find_all("div","superPageFontColor")[1].find_all("span")[1].get_text()

    source = db.SOURCES["RottenTomatoes"]

    params = json.dumps(
        {
            "source": "",#source,
            "movie": movie_id,
            "sourceid": sourceid,
            "name": "RottenTomatoesExpert",
            "rating": rating,
            "count": count
        }
    )

    db.insert_data(db.API_URLS["rating"], params)


# insert_audience(soup, movie_id, sourceid, db), insert audience rating
#                                          of Rotten Tomatoes,
#   Params
#       - soup, page from BeautifulSoup
#       - movie_id, id of the movie in mooviest db
#       - sourceid, sourceid from mooviest db
#       - db, interface db
def insert_audience(soup, movie_id, sourceid, db):

    # AUDIENCE SCORE - RottenTomatoesAudience
    # Div with RottenTomatoesAudience
    lista = soup.find_all("div", {"class":"audiencepanel"})[0]
    # Rating
    rating = lista.find_all("div", {"class":"audience-score meter"})[0].find("span","superPageFontColor").get_text()
    rating = int(rating.replace("%", ""))
    # Count
    count = lista.find("div","audience-info").find_all("div")[1].get_text()
    count = int(count.replace("User Ratings:", "").strip().replace(",",""))

    source = db.SOURCES["RottenTomatoes"]

    params = json.dumps(
        {
            "source": "",#source,
            "movie": movie_id,
            "sourceid": sourceid,
            "name": "RottenTomatoesAudience",
            "rating": rating,
            "count": count
        }
    )

    db.insert_data(db.API_URLS["rating"], params)


# insert_rating(db, movie_id, url_rotten), insert expert and audience rating
#                                          of Rotten Tomatoes,
#   Params
#       - db, interface db
#       - movie_id, id of the movie in mooviest db
#       - url_rotten, sourceid for make the url of Rotten Tomatoes
def insert_rating(db, movie_id, url_rotten):

    error_message = "Movie id: " + str(movie_id) + " - Script rating Rotten Tomatoes\n"
    error_code = 0
    error_call = 0

    try:
        url = "https://www.rottentomatoes.com/m/" + url_rotten + "/"
        response = urllib.request.urlopen(url)
        html = response.read().decode("utf8")
        soup = BeautifulSoup(html, 'html.parser')

    except:
        error_message += "Error call url: " + url + "\n"
        error_code = 1
        error_call = 1

    if (error_call == 0):
        try:
            # Insert expert rating
            insert_expert(soup, movie_id, url_rotten, db)
        except:
            error_message += "Error insert expert rating: " + url + "\n"
            error_code = 1

        try:
            # Insert audience rating
            insert_audience(soup, movie_id, url_rotten, db)
        except:
            error_message += "Error insert audience rating: " + url + "\n"
            error_code = 1

    return error_code, error_message
