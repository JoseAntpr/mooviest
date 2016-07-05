import urllib.request, json
from bs4 import BeautifulSoup

# film name of the film in spanish
# return, the rating and the number ratings of the film
def rating_filmaffinity(film):
    search = film.replace(" ","+")
    url = "http://www.filmaffinity.com/es/search.php?stext="+search+"&stype=all"
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
            print(film+" rating:_, count:_")

    rating = int(rating_str.replace(",", ""))
    count = int(count_str.replace(".", ""))
    id_movie = int(id_str.replace("/es/film","").replace(".html",""))
    return id_movie,rating,count

#example, call function rating_filmaffinity
i,r,c = rating_filmaffinity("E.T., el extraterrestre")
#i,r,c = rating_filmaffinity("Los juegos del hambre")

print(i)
print(r)
print(c)
