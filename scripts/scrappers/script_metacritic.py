import urllib.request, json
from bs4 import BeautifulSoup

# get_url_metacritic_by_imdb(imdb), return metacritic url by imdb
#
#   Params
#       - imdb, movie id of imdb

def get_url_metacritic_by_imdb(imdb):
    url = "http://www.imdb.com/title/"+imdb+"/criticreviews?ref_=tt_ov_rt"
    response = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(response).read()
    soup = BeautifulSoup(html, 'html.parser')

    lista = soup.find_all("div",{"class":"see-more"})
    url_metacritic = ""
    if len(lista) > 0:
        url_metacritic = lista[0].find_all("a")[0].get('href')

    return url_metacritic


# insert_rating(url,movie_id), insert rating, count and id movie if exits
#                  of FilmAffinitty, with name(in spanish) film
#   Params
#       - c, conection Api
#       - headers, headears request
#       - movie_name, name(in spanish) of the movie
#       - movie_id, id of the movie in mooviest db

def insert_rating(db, movie_id, url):

    response = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(response).read()
    soup = BeautifulSoup(html, 'html.parser')

    rating = 0
    count = 0
    lista = soup.find_all("div",{"class":"user"})
    if len(lista) > 0:
        rating = lista[0].get_text().strip()
        lista = soup.find_all("div",{"class":"details side_details"})
        lista = lista[0].find_all("span",{"class":"count"})
        count = lista[0].find("a").get_text().lower()
        count = count.replace("ratings","").strip()
        rating = int(count.replace(".", "").replace(",", ""))
        count = int(count.replace(".", "").replace(",", ""))
    else:
        return movie_id+" rating_metacritic:_, count:_"

    sourceid = url
    source = db.SOURCES["Metacritic"]
    params = json.dumps(
        {
            "source": source,
            "movie": movie_id,
            "sourceid": sourceid,
            "name": "Metacritic",
            "rating": rating,
            "count": count
        }
    )
    return db.insert_data(db.API_URLS["rating"], params)

#example, call function rating_metacritic
