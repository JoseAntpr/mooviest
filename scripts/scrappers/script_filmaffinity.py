import psycopg2, urllib.request, urllib.parse, http.client, json
from base64 import b64encode
from bs4 import BeautifulSoup


# Contants
api_url = '/api/rating/'

# insert_countries(c, headers, movie_name, movie_id), insert rating, count and id movie
#                  of FilmAffinitty, with name(in spanish) film
#   Params
#       - c, conection Api
#       - headers, headears request
#       - movie_name, name(in spanish) of the movie
#       - movie_id, id of the movie in mooviest db

def insert_rating(db, movie_id, movie_name):
    #search = movie_name.replace(" ","+")
    search = urllib.parse.quote_plus(movie_name)
    print(search)
    url = "http://www.filmaffinity.com/es/search.php?stext="+search+"&stype=all"
    print(url)
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf8")
    soup = BeautifulSoup(html, 'html.parser')

    id_str = ""
    rating_str = ""
    count_str = ""
    lista = soup.find_all("div",{"class":"avgrat-box"})


    if len(lista) > 0:
        rating_str = lista[0].get_text().strip()
        lista = soup.find_all("div",{"class":"ratcount-box"})
        count_str = lista[0].get_text().strip()
        id_str = soup.find_all("div",{"class":"mc-title"})[0]
        id_str = id_str.find_all("a")[0].get('href')
    else:
        try:
            rating_str = soup.find(id="movie-rat-avg").get_text().strip()
            count_str = soup.find(itemprop="ratingCount").get_text().strip()
            id_str = soup.find_all("li",{"class":"active"})[0].find('a').get('href')
        except AttributeError:
            rating_str = "0"
            count_str = "0"
            print(movie_name+" rating:_, count:_")

    rating = int(rating_str.replace(",", ""))
    count = int(count_str.replace(".", ""))
    sourceid = int(id_str.replace("/es/film","").replace(".html",""))
    source = db.SOURCES["FilmAffinity"]

    params = json.dumps(
        {
            "source": source,
            "movie": movie_id,
            "sourceid": sourceid,
            "rating": rating,
            "count": count
        }
    )

    return db.insert_data(api_url, params)
