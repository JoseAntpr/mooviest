import urllib.request, urllib.parse, http.client, json
from base64 import b64encode
from bs4 import BeautifulSoup

def insert_rating(db, movie_id, id_imdb):

    url = "http://www.imdb.com/title/" + id_imdb + "/"
    print(url)
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf8")
    soup = BeautifulSoup(html, 'html.parser')

    rating = ""
    count = ""
    lista = soup.find_all("div",{"class":"ratingValue"})

    print(lista)
    print(len(lista))
    if len(lista) > 0:
        try:
            rating = soup.find(itemprop="ratingValue").get_text().strip()
            count = soup.find(itemprop="ratingCount").get_text().strip()

            rating = int(rating.replace(".", ""))
            count = int(count.replace(",", ""))
        except AttributeError:
            rating = 0
            count = 0

    source = db.SOURCES["IMDb"]

    params = json.dumps(
        {
            "source": source,
            "movie": movie_id,
            "sourceid": id_imdb,
            "rating": rating,
            "count": count
        }
    )

    return db.insert_data(db.API_URLS["rating"], params)
