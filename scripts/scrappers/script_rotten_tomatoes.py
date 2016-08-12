import urllib.request, urllib.parse, http.client, json
from base64 import b64encode
from bs4 import BeautifulSoup

def insert_rating(db, movie_id, id_imdb):

    url = "http://www.omdbapi.com/?i=" + id_imdb + "&tomatoes=true&plot=full&r=json"

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf8"))
        url_rotten = data["tomatoURL"]

        url_rotten = str(url_rotten.replace("http://www.rottentomatoes.com/m/", ""))

        print(url_rotten)

        url = "https://www.rottentomatoes.com/m/" + url_rotten
        print(url)
        response = urllib.request.urlopen(url)
        html = response.read().decode("utf8")
        soup = BeautifulSoup(html, 'html.parser')


    except:
        print("error")

insert_rating(1, 1, "tt1289401")
