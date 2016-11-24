import urllib.request, json
from bs4 import BeautifulSoup
from .import interface


# get_url_metacritic_by_imdb(imdb), return metacritic url by imdb
#
#   Params
#       - imdb, movie id of imdb
#
def get_url_metacritic_by_imdb(imdb):
    error_message = ""
    url = "http://www.imdb.com/title/"+imdb+"/criticreviews?ref_=tt_ov_rt"
    error_code = False
    url_metacritic = ""

    error_code, error_message, soup = interface.get_soup(url)
    if error_code:
        return error_code, error_message, url_metacritic

    try:
        lista = soup.find_all("div",{"class":"see-more"})
        if len(lista) > 0:
            url_metacritic = lista[0].find_all("a")[0].get('href')
            if url_metacritic.find("/lists/") != -1:
                error_code = True
        else:
            error_code = True
    except:
        error_code = True

    if error_code:
        error_message += "Error get url of metacritic, imdb page url: "+url+"\n"
        return error_code, error_message, url_metacritic

    return error_code, error_message, url_metacritic

# format_params(rating, count), sourceid returns, rating formatted
#
#   Params
#       - rating, rating of Metacritic
#       - count, count of Metacritic
#
def format_params(rating,count,count2,count3):
    error_code = False
    error_message = ""
    try:
        rating = int(rating.replace(".", "").replace(",", ""))
        count = int(count.replace(".", "").replace(",", ""))
        count += int(count2.replace(".", "").replace(",", ""))
        count += int(count3.replace(".", "").replace(",", ""))
    except:
        rating = 0
        count = 0
        error_code = True
        error_message = "Error format params, rating Metacritic\n"

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
    count = 0
    try:
        countp = soup.find_all("div",{"class":"count"})
        rating = soup.find_all("span",{"class":"user"})[0].get_text().strip()
        countPositive = soup.find_all("div",{"class":"count"})[3].get_text().strip()
        countMixed = soup.find_all("div",{"class":"count"})[4].get_text().strip()
        countNegative = soup.find_all("div",{"class":"count"})[5].get_text().strip()
    except:
        rating = ""
        count = 0
        error_code = True
        error_message = "Error get audience, rating Metacritic\n"
    if error_code:
        return error_code, error_message, rating, count
    return format_params(rating, countPositive, countMixed, countNegative)

# get_rating_expert(soup): sourceid returns, rating and count formatted
#
#   Params
#       - soup, soup Metacritic movie page
#
def get_rating_expert(soup):
    error_code = False
    error_message = ""
    rating = ""
    count = "0"
    try:
        rating = soup.find_all("span",{"class":"metascore_w"})[0].get_text().strip()
        countPositive = soup.find_all("div",{"class":"count"})[0].get_text().strip()
        countMixed = soup.find_all("div",{"class":"count"})[1].get_text().strip()
        countNegative = soup.find_all("div",{"class":"count"})[2].get_text().strip()
    except:
        rating = ""
        count = "0"
        error_code = True
        error_message = "Error get expert, rating Metacritic\n"
    if error_code:
        return error_code, error_message, rating, count

    return format_params(rating, countPositive,countMixed,countNegative)

# insert(db, movie_id, url, soup, expert), insert rating in mooviest db
#
#   Params
#       - db, Object DB
#       - movie_id, id of the movie in mooviest db
#       - rating_id, id of rating
#       - url, url of Metacritic
#       - soup, soup Metacritic movie page
#       - expert, True if expert anf False if audience
def insert(db, movie_id, url, soup, expert):
    error_code = False
    error_message = ""
    res = {}
    rating = 0
    count = 0
    name = "MetacriticAudience"
    if expert:
        error_code, msg, rating, count = get_rating_expert(soup)
        name = "MetacriticExpert"
    else:
        error_code, msg, rating, count = get_rating(soup)

    if error_code:
        error_message += msg
        return error_code, error_message, res

    sourceid = url.replace("http://www.metacritic.com/movie/", "")
    params = json.dumps(
        {
            "source": db.SOURCES["Metacritic"],
            "movie": movie_id,
            "sourceid": sourceid,
            "name": name,
            "rating": rating,
            "count": count
        }
    )

    try:
        res = db.insert_data(db.API_URLS["rating"], params)
    except:
        error_code = True
        error_message += "Error insert, rating Metacritic"

    return error_code, error_message, res

# update(db, rating_id, soup, expert), update rating in mooviest db
#
#   Params
#       - db, Object DB
#       - rating_id, id of rating
#       - soup, soup Metacritic movie page
#       - expert, True if expert anf False if audience
def update(db, rating_id, soup, expert):
    error_code = False
    error_message = ""
    rating = 0
    count = 0
    res = {}

    if expert:
        error_code, msg, rating, count = get_rating_expert(soup)
    else:
        error_code, msg, rating, count = get_rating(soup)

    if error_code:
        error_message += msg
        return error_code, error_message, res

    params = json.dumps(
        {
            "rating": rating,
            "count": count
        }
    )

    try:
        db.update_data(db.API_URLS["rating"]+str(rating_id)+"/", params)
    except:
        error_message +"Error update, rating Metacritic"
        error_code = True

    return error_code, error_message, res

# insert_rating(db, movie_name, movie_id), insert rating, count and id movie
#                  of Metacritic
#   Params
#       - db, Object DB
#       - movie_id, id of the movie in mooviest db
#       - imdb, id movie of imdb
def insert_rating(db, movie_id, imdb):
    error_message = ""
    res = {}

    error_code, msg, url = get_url_metacritic_by_imdb(imdb)
    if error_code:
        error_message += msg
        return error_code, error_message, res, res


    error_code, msg, soup = interface.get_soup(url)
    if error_code:
        error_message += msg
        return error_code, error_message, res, res

    error_code, msg, res = insert(db, movie_id, url, soup, False)
    error_message += msg

    error_code_expert, msg, res_expert = insert(db, movie_id, url, soup, True)
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
    res = {}

    error_code, msg, soup = interface.get_soup(sourceid)
    if error_code:
        error_message += msg
        return error_code, error_message, res, res

    error_code, msg, res = update(db, rating_id, soup, False)
    error_message += msg

    error_code_expert, msg, res_expert = update(db, rating_expert_id, soup, True)
    error_message += msg

    return (error_code or error_code_expert), error_message, res, res_expert

# id_imdb = "tt0120737"
#
# # error_code, msg, url= get_url_metacritic_by_imdb(id_imdb)
# # print(error_code, msg, url)
# url = "http://www.metacritic.com/movie/rules-dont-apply"
# error_code, msg, soup = interface.get_soup(url)
# # print(error_code, msg, soup)
#
# error_code, error_message, rating, count = get_rating(soup)
# print("rating:",rating,count)
# error_code, error_message, rating, count = get_rating_expert(soup)
# print("rating expert:",rating,count)

# error_code, msg, res = insert(db, movie_id, url, soup, False)
# error_message += msg
#
# error_code_expert, msg, res_expert = insert(db, movie_id, url, soup, True)
# error_message += msg
#
# return (error_code or error_code_expert), error_message, res, res_expert
