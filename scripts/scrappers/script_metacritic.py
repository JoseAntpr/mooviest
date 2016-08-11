import urllib.request, json
from bs4 import BeautifulSoup

# film name of the film in english
# return, the id, the rating and the number ratings of the film
def rating_metracritic(film):
    search = film.replace(".","")
    search = search.replace(",","")
    search = search.replace(":","")
    search = search.replace(" ","-")
    url = "http://www.metacritic.com/movie/"+search.lower()
    print(url)

    response = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(response).read()
    soup = BeautifulSoup(html, 'html.parser')

    rating_str = "0"
    count_str = "0"
    lista = soup.find_all("div",{"class":"user"})
    if len(lista) > 0:
        rating_str = lista[0].get_text().strip()
        lista = soup.find_all("div",{"class":"details side_details"})
        lista = lista[0].find_all("span",{"class":"count"})
        count_str = lista[0].find("a").get_text().lower()
        count_str = count_str.replace("ratings","").strip()
        rating = int(rating_str.replace(".", "").replace(",", ""))
        count = int(count_str.replace(".", "").replace(",", ""))
    else:
        rating_str = "0"
        count_str = "0"
        print(film+" rating:_, count:_")



    return search.lower(),rating,count




#example, call function rating_metracritic
i,r,c = rating_metracritic("E.T. The Extra-Terrestrial")

print(i)
print(r)
print(c)
