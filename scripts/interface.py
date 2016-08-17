import smtplib, email, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Constants send email
gmail_password = 'jscj1618'
fromaddr = 'mooviest@gmail.com'
toaddr = ['jasus77@gmail.com','jasus_7@hotmail.com']


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

def save_lastline(filename,idm):
	f = open(filename,'w')
	lastline = str(idm)
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
