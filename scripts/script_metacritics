import psycopg2, urllib.request, json
#Token api

#http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json?apikey=[your_api_key]&type=imdb&id=0031381
#try:
#	db = psycopg2.connect("dbname='mooviest' user='jesus' host='localhost' password='root'")
#except:
#	print("Error connecting to database")

idmovie = "2488496" #star wars
auth_token = "token"
url = "http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json?apikey=" + auth_token + "&type=imdb&id=" + idmovie
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode("utf8"))
rating = int(data["ratings"]["critics_score"])
