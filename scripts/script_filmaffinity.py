import urllib.request, json
from bs4 import BeautifulSoup

# film name of the film in spanish
# return, The rating and th number ratings of the film
def rating_filmaffinity(film):
    search = film.replace(" ","+")
    url = "http://www.filmaffinity.com/es/search.php?stext="+search+"&stype=all"
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf8")
    soup = BeautifulSoup(html, 'html.parser')

    lista = soup.find_all("div",{"class":"avgrat-box"})
    rating_str = ""
    count_str = ""
    if len(lista) > 0:
        rating_str = lista[0].get_text()
        lista = soup.find_all("div",{"class":"ratcount-box"})
        count_str = lista[0].get_text()
    else:
        rating_str = soup.find(id="movie-rat-avg").get_text().strip()
        count_str = soup.find(itemprop="ratingCount").get_text()

    rating = int(rating_str.replace(",", ""))
    count = int(count_str.replace(".", ""))

    return rating,count

#example, call function rating_filmaffinity
r,c = rating_filmaffinity("E.T., el extraterrestre")

print(r)
print(c)
