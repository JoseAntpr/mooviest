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

    rating_str = ""
    count_str = ""
    lista = soup.find_all("div",{"class":"avgrat-box"})

    if len(lista) > 0:
        rating_str = lista[0].get_text().strip()
        lista = soup.find_all("div",{"class":"ratcount-box"})
        count_str = lista[0].get_text().strip()
    else:
        try:
            rating_str = soup.find(id="movie-rat-avg").get_text().strip()
            count_str = soup.find(itemprop="ratingCount").get_text().strip()
        except AttributeError:
            rating_str = "0"
            count_str = "0"
            print(film+" rating:_, count:_")

    rating = int(rating_str.replace(",", ""))
    count = int(count_str.replace(".", ""))

    return rating,count

#example, call function rating_filmaffinity
r,c = rating_filmaffinity("E.T., el extraterrestre")
#r,c = rating_filmaffinity("Los juegos del hambre")

print(r)
print(c)
