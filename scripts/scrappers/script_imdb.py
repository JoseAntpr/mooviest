import urllib.request, json
from bs4 import BeautifulSoup
from . import interface

# get_rating(soup), get rating of IMDb,
#   Params
#       - soup, page from BeautifulSoup
def get_rating(soup):

    rating = soup.find(itemprop="ratingValue").get_text().strip()
    count = soup.find(itemprop="ratingCount").get_text().strip()

    rating = int(rating.replace(".", ""))
    count = int(count.replace(",", ""))

    return rating, count

# insert_rating(db, movie_id, imdb_id), insert rating of IMDb,
#   Params
#       - db, interface db
#       - movie_id, id of the movie in mooviest db
#       - imdb_id, id of IMDb
def insert_rating(db, movie_id, imdb_id):

    url = "http://www.imdb.com/title/" + imdb_id + "/"
    error_message = "Movie id: " + str(movie_id) + " - Script INSERT rating IMDb\n URL:" + url + "\n"
    res = {}

    # Get soup from url
    error_code, msg, soup = interface.get_soup(url)

    if not error_code:

        try:
            # Get IMDb rating
            rating, count = get_rating(soup)
            params = json.dumps(
                {
                    "source": db.SOURCES["IMDb"],
                    "movie": movie_id,
                    "sourceid": imdb_id,
                    "rating": rating,
                    "count": count
                }
            )

            res = db.insert_data(db.API_URLS["rating"], params)

        except:
            error_message += "Error insert rating\n"
            error_code = True

    else:
        error_message += msg

    return error_code, error_message, res

# update_rating(db, rating_id, imdb_id), update rating of IMDb,
#   Params
#       - db, interface db
#       - rating_id, rating id to update
#       - imdb_id, id of IMDb
def update_rating(db, rating_id, imdb_id):

    url = "http://www.imdb.com/title/" + imdb_id + "/"
    error_message = "Rating id: " + str(rating_id) + " - Script UPDATE rating IMDb\n URL:" + url + "\n"
    res = {}

    # Get soup from url
    error_code, msg, soup = interface.get_soup(url)

    if not error_code:

        try:
            # Get IMDb rating
            rating, count = get_rating(soup)
            params = json.dumps(
                {
                    "rating": rating,
                    "count": count
                }
            )

            res = db.update_data(db.API_URLS["rating"] + rating_id + "/", params)

        except:
            error_message += "Error update rating\n"
            error_code = True

    else:
        error_message += msg

    return error_code, error_message, res
