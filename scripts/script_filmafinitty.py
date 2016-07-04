import urllib.request, json
from bs4 import BeautifulSoup
#Token api

#https://www.filmaffinity.com/en/evideos.php?movie_id=859120
#try:
#	db = psycopg2.connect("dbname='mooviest' user='jesus' host='localhost' password='root'")
#except:
#	print("Error connecting to database")

idmovie = "859120" #star wars
#url = "https://www.filmaffinity.com/en/evideos.php?movie_id=" + idmovie
url = "http://www.filmaffinity.com/es/search.php?stext=los+juegos+del+hambre&stype=all"
response = urllib.request.urlopen(url)
html = response.read().decode("utf8")
soup = BeautifulSoup(html, 'html.parser')

#soup.find_all('div')
#rating = soup.find(id="movie-rat-avg").get_text()
#count = soup.find(id="movie-count-rat").get_text()
rating = soup.find_all("div",{"class":"ratcount-box"})[0].get_text()
#count = soup.find(class="ratcount-box").get_text()
print(rating)
#print(count)
##movie-count-rat
