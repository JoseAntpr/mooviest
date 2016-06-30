import psycopg2, urllib.request, json

id_api = '3504'
secret = 'bhRNt7TaHhuVcKxExK3n'
auth_token = json.loads(urllib.request.urlopen('https://api.tviso.com/auth_token?id_api=' + id_api + '&secret=' + secret).read().decode('utf8'))["auth_token"]
mediaType = '2'


#try:
#	db = psycopg2.connect("dbname='mooviest' user='jesus' host='localhost' password='root'")
#except:
#	print("Error connecting to database")

cur = db.cursor()

for i in range(0, 1000):
	print(i)
	idm = str(i)
	url = "https://api.tviso.com/media/full_info?auth_token=" + auth_token + "&idm=" + idm  + "&mediaType=" + mediaType
	response = urllib.request.urlopen(url)
	data = json.loads(response.read().decode("utf8"))

	error = data["error"]

	if error == 1:
		print('error: Auth token')
	elif error == 9 || error == 50:
		print('error: Media type')
	elif error == 10:
		print('error: Idm')
	elif error == 803:
		print('error: Media limit reached at number ' + i)
		break
	else:

		# MOVIE
		runtime = int(data["runtime"])
		released = int(data["year"])

		movie_producer_list = []
		try:
			for produce in data["produce"]
				movie_producer_list.append(produce["name"])
		except IndexError:
			movie_producer_list = []

		genre_list = []
		try:
			for index, genre in enumerate(data["genres"], start=0)
				genre_list.append(genre[index])
		except IndexError:
			genre_list = []

		# MOVIE LANG
		title = str(data["name"])

		director_list = []
		for director in data["director"]:
			director_list.append(director["name"])

		director = ', '.join(director_list)

		casting_list = []
		for actor in data["cast"]:
			casting_list.append(actor["name"])

		casting = ', '.join(casting_list)

		plot = str(data["plot"])



		remote_poster = "https://img.tviso.com/ES/poster/w430" + str(data["images"]["poster"])
		try:
			genre = ', '.join(data["genres"])
		except KeyError:
			genre = ""

		rating_tviso = data["rating"]
		id_imdb = data["imdb"]
		id_tviso = data["idm"]

		if(id_imdb):
			#Obtain IMDb ratings from OMDb API
			url_omdb ="http://www.omdbapi.com/?i=" + id_imdb + "&plot=short&r=json"
			response_omdb = urllib.request.urlopen(url_omdb)
			data_omdb = json.loads(response_omdb.read().decode("utf8"))
			try:
				rating_imdb = float(data_omdb["imdbRating"])
			except ValueError:
				rating_imdb = ""

			cur.execute("""INSERT INTO mooviestapp_movie (title, director, casting, plot, producer, remote_poster, genre, released)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;""", (title, director, casting, plot, producer, remote_poster, genre, released))

			movie_id = cur.fetchone()[0]
			cur.execute("""INSERT INTO mooviestapp_rating (movie_id, source, rating, source_id) VALUES (%s, %s, %s, %s);""", (movie_id, "Tviso", rating_tviso, id_tviso))

			if(rating_imdb):
				cur.execute("""INSERT INTO mooviestapp_rating (movie_id, source, rating, source_id) VALUES (%s, %s, %s, %s);""", (movie_id, "IMDb", rating_imdb, id_imdb))


db.commit()
cur.close()
db.close()
