import smtplib, email, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Constants txts
lastline_txt = "lastline.txt"
datos_sin_numero_txt = "datos_sin_numero.txt"
log_txt = "log.txt"

# Constants send email
gmail_password = "jscj1618"
fromaddr = "mooviest@gmail.com"
toaddr = ["jasus77@gmail.com","guezo983@gmail.com",""]


# send_mail, send an email to addresses of toaddr
def send_mail():

	f = open(log_txt)
	msg_email = "".join(f.readlines())

	msg = MIMEMultipart()
	msg["From"] = fromaddr
	msg["To"] = ", ".join(toaddr)
	msg["Subject"] = "Error in script ids Tviso to txt"

	body = msg_email
	msg.attach(MIMEText(body, "plain"))


	server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server.ehlo()
	server.login(fromaddr, gmail_password)
	email_text = msg.as_string()
	server.sendmail(fromaddr, toaddr, email_text)
	server.close()

def save_lastline(filename,idm):
	f = open(filename,'w')
	lastline = str(idm+1)
	f.write(lastline)
	f.close()

def get_lastline(filename):
	f = open(filename,'r')
	lastline = f.readline()
	f.close()
	return int(lastline)-1

def get_ids(filename):
	ids = []
	with open(filename) as f:
	    ids = f.readlines()
	    f.close()
	return ids

def save_log(filename, msg):
	f = open(filename, 'a')
	f.write(msg)
	f.close()
