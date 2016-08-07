import  urllib.parse, http.client, json
from base64 import b64encode
#

def insert_genres(c,userAndPass,headers):
	genres=['action',
			'comedy',
			'family',
			'history',
			'mystery',
			'sci-fi',
			'war',
			'adventure',
			'crime',
			'fantasy',
			'horror',
			'news',
			'sport',
			'western',
			'animation',
			'documentary',
			'film-noir',
			'music',
			'drama',
			'musical',
			'romance',
			'thriller',
			'reallity']

	for i in range(0,len(genres)):
		params = urllib.parse.urlencode({'code': genres[i]})
		c.request('POST', '/api/genre/', params, headers)
		#get the response back
		res = c.getresponse()
		print(res.status, res.reason)
		# at this point you could check the status etc
		# this gets the page text
		data = res.read()

def insert_genres_lang(c,userAndPass,headers):
	genres_lang=[['Action',
			'Comedy',
			'Family',
			'History',
			'Mystery',
			'Sci-fi',
			'War',
			'Adventure',
			'Crime',
			'Fantasy',
			'Horror',
			'News',
			'Sport',
			'Western',
			'Animation',
			'Documentary',
			'Film-noir',
			'Music',
			'Drama',
			'Musical',
			'Romance',
			'Thriller',
			'Reallity'],
			['Acción',
			'Comedia',
			'Familiar',
			'Histórico',
			'Misterio',
			'Ciencia ficción',
			'Bélico',
			'Aventura',
			'Crimen',
			'Fantasía',
			'Horror',
			'Actualidad',
			'Deportes',
			'Western',
			'Animación',
			'Documental',
			'Cine negro',
			'Musical',
			'Drama',
			'Musical',
			'Romance',
			'Thriller',
			'Reallity show']]

	for i in range(0,len(genres_lang)):
		for j in range(0,len(genres_lang[0])):
			params = urllib.parse.urlencode(
				{
					"genre": (j+1),
				    "lang": (i+1),
				    "name": genres_lang[i][j]
				}
			)
			c.request('POST', '/api/genre_lang/', params, headers)
			#get the response back
			res = c.getresponse()
			print(res.status, res.reason)
			# at this point you could check the status etc
			# this gets the page text
			data = res.read()
