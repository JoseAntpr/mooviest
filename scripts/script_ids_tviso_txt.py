import urllib.request, json, time

id_api = '3504'
secret = 'bhRNt7TaHhuVcKxExK3n'
auth_token = json.loads(urllib.request.urlopen('https://api.tviso.com/auth_token?id_api=' + id_api + '&secret=' + secret).read().decode('utf8'))["auth_token"]
mediaType = '2'
archivo=open('datos.txt','a')

#try:
#	db = psycopg2.connect("dbname='mooviest' user='jesus' host='localhost' password='root'")
#except:
#	print("Error connecting to database")

# cur = db.cursor()

for i in range(252226, 1000000):
	idm = str(i)
	url = "https://api.tviso.com/media/basic_info?auth_token=" + auth_token + "&idm=" + idm  + "&mediaType=" + mediaType
#	time.sleep(1)
	response = urllib.request.urlopen(url)

	data = json.loads(response.read().decode("utf8"))

	error = data["error"]

	if error == 1:
		print('error: Auth token')
	elif(error == 9 or error == 50):
		print(idm+' - error: Media type')
	elif error == 10:
		print(idm+' - error: Idm')
	elif error == 20:
		print(idm+' - error: Quota exceeded')
		archivo.close()
		break
	elif error == 803:
		print('error: Media limit reached at number ' + idm)
		archivo.close()
		break
	else:

		id_tviso = str(data["idm"])
		archivo.write(id_tviso+'\n')


#db.commit()
#cur.close()
#db.close()
archivo.close()
