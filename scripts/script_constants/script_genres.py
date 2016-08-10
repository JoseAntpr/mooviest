import  urllib.parse, http.client, json
from base64 import b64encode
import script_interface as interface

# Contants
api_url_genres = '/api/genre/'
api_url_genres_lang = '/api/genre_lang/'


# insert_genres(c, headers), insert all genres in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_genres(c, headers):
	genres = [
				'action', 'comedy', 'family', 'history', 'mystery',
				'sci-fi', 'war', 'adventure', 'crime', 'fantasy',
				'horror', 'news', 'sport', 'western', 'animation',
				'documentary', 'film-noir', 'music', 'drama',
				'musical', 'romance', 'thriller', 'reallity'
			]

	for genre in genres:
		params = json.dumps({'code': genre})
		interface.insert_data(c, api_url_genres, params, headers)

# insert_genres_lang(c, headers), insert all genres_lang in to th DB
#   Params
#       - c, conection Api
#       - headers, headears request

def insert_genres_lang(c, headers):
	genres_lang = [
		[
			'Action', 'Comedy', 'Family', 'History', 'Mystery',
			'Sci-fi', 'War', 'Adventure', 'Crime', 'Fantasy', 'Horror',
			'News', 'Sport', 'Western', 'Animation', 'Documentary',
			'Film-noir', 'Music', 'Drama', 'Musical', 'Romance',
			'Thriller', 'Reallity'
		],
		[
			'Acción', 'Comedia', 'Familiar', 'Histórico', 'Misterio',
			'Ciencia ficción', 'Bélico', 'Aventura', 'Crimen', 'Fantasía',
			'Horror', 'Actualidad', 'Deportes', 'Western', 'Animación',
			'Documental', 'Cine negro', 'Musical', 'Drama', 'Musical',
			'Romance', 'Thriller', 'Reallity show'
		]
	]

	for i in range(0,len(genres_lang)):
		for j in range(0,len(genres_lang[0])):
			params = json.dumps(
				{
					"genre": (j+1),
				    "lang": (i+1),
				    "name": genres_lang[i][j]
				}
			)
			interface.insert_data(c, api_url_genres_lang, params, headers)
