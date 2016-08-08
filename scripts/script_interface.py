import psycopg2, urllib.request, urllib.parse, http.client, json, smtplib, email, time
from base64 import b64encode
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Constants Tviso
id_api = '3504'
secret = 'bhRNt7TaHhuVcKxExK3n'
mediaType = "2"

# Constants send email
gmail_password = 'jscj1618'
fromaddr = 'mooviest@gmail.com'
toaddr = ['jasus77@gmail.com','jasus_7@hotmail.com']


# Constants app
langs = { "en": 1, "es": 2}

sources = {
	'FilmAffinity':		1,
	'Sensacine':		2,
 	'Tviso':			3,
	'Track.tv':			4,
	'IMDb':				5,
	'Metacritic':		6,
	'RottenTomatoes':	7,
	'Letterboxd':		8
}

countries=[
	{
		'ES': 1,
		'DE': 2,
		'IT': 3,
		'FR': 4,
		'GB': 5,
		'US': 6,
		'AR': 7,
		'MX': 8,
		'XX': 9
	},
	{
		'ES': 10,
		'DE': 11,
		'IT': 12,
		'FR': 13,
		'GB': 14,
		'US': 15,
		'AR': 16,
		'MX': 17,
		'XX': 18
	}
]

def get_token():
	return json.loads(urllib.request.urlopen('https://api.tviso.com/auth_token?id_api=' + id_api + '&secret=' + secret).read().decode('utf8'))["auth_token"]

def insert_data(c, api_url, js, headers):

    c.request('POST', api_url, js, headers)
    res = c.getresponse()
    print(res.status, res.reason)
    data = res.read()

	return data

# get_info_tviso, return data format json, of the media with idm
#   Params
#       - idm, id(Tviso) of the media
#       - auth_token, token of the API Tviso, generate with the data mooviest
#       - mediaType, type of media, 1-Serie/2-Movie/3-TvShow/4-Docu/5-Capitulo
#   if all ok, data["error"] == 0
def get_info_tviso(idm, auth_token):
    url = "https://api.tviso.com/media/full_info?auth_token=" + auth_token + "&idm=" + idm  + "&mediaType=" + mediaType

	try:
		response = urllib.request.urlopen(url)
	    data = json.loads(response.read().decode("utf8"))
	    error = data["error"]
	except:
		error = 502

	if error == 1:
		error_msg = 'error: Auth token'
		print(error_msg)

		send_mail(idm, error_msg)
		auth_token = get_token()

	elif(error == 9 or error == 50):
		print(idm+' - error: Media type')

	elif error == 10:
		print(idm+' - error: Idm')

	elif error == 20:
		error_msg = 'error: Quota exceeded'
		print(idm+' - '+error_msg)

		save_lastid(idm)
		send_mail(idm, error_msg)
		break

	elif error == 502:
		error_msg = 'error: Response timeout or internet connection is not available'
		print(idm+' - '+error_msg)

		send_mail(idm, error_msg)

	elif error == 803:
		error_msg = 'error: Media limit reached'
		print(idm+' - '+error_msg)
		break

	else:

	return data, error

# send_mail, send an email to addresses of toaddr
def send_mail(id_tviso, error):

	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = ', '.join(toaddr)
	msg['Subject'] = "Error in script ids Tviso to txt"

	body = "Hey, what's man?\n\n- "+error+" at id: "+id_tviso
	msg.attach(MIMEText(body, 'plain'))


	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(fromaddr, gmail_password)
	email_text = msg.as_string()
	server.sendmail(fromaddr, toaddr, email_text)
	server.close()

	print("Email sent!")

def save_lastid(idm):
	f = open('lastid.txt','w')
	lastid = str(idm)
	f.write(lastid)
	f.close()
