import json
import interface_db

def get_lineas(filename):
	lineas = []
	with open(filename) as f:
	    lineas = f.readlines()
	    f.close()
	return lineas

def get_logs(lineas):
    logs = []
    buff = ""
    for linea in lineas:
        if linea == "\n":
            logs.append(buff)
            buff = ""
        else:
            buff += linea
    return logs

def get_log_line(log, i):
    lineas = log.split("\n")
    return lineas[i]

def group_by_text(logs,s):
    group = []
    for log in logs:
        if log.find(s) >= 0:
            group.append(log)
    return group

def scraper_tviso(log_tviso):
    lineas = log_tviso.split("\n")
    idm = int(lineas[0].replace("Movie idm: ","").replace(" - Script info_movie",""))
    mooviest_id = int(lineas[2].replace("Mooviest id: ",""))
    return mooviest_id, idm, "Tviso"

def scraper_imdb(log_imdb):
    lineas = log_imdb.split("\n")
    imdb = lineas[1].replace("Imdb: ","").strip()
    mooviest_id = int(lineas[2].replace("Mooviest id: ",""))
    return mooviest_id, imdb, "IMDb"

def scraper_ratings(db, function, logs):
    ratings = []
    for log in logs:
        movie, sourceid, source_name = function(log)
        rating = {
            "source": db.SOURCES[source_name],
            "movie": movie,
            "sourceid": sourceid,
            "name": source_name,
            "rating": 0,
            "count": 0
        }
        ratings.append(rating)
    return ratings

def insert_ratings(db, ratings):
	for rating in ratings:
		res = db.insert_data(db.API_URLS["rating"], json.dumps(rating))
		try:
			res["id"]
			print("Insertado rating correctamente res: "+str(res))
		except:
			print("Error insert rating res: "+str(res))



db = interface_db.DB("admin","admin")
ls = get_lineas("log.txt")
lgs = get_logs(ls)
group = group_by_text(lgs,"rating")
tviso = group_by_text(group,"Tviso")
imdb = group_by_text(group,"IMDb")

tviso = scraper_ratings(db,scraper_tviso, tviso)
imdb = scraper_ratings(db,scraper_imdb, imdb)

insert_ratings(db,tviso)
insert_ratings(db,imdb)
