import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
class email():
	def configure(self,sender, password):
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.server.login(sender, password)

	def send_email(self,sender,password,argv,receivers, subject='Generated Caption - Drishti '):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(sender, password)
		COMMASPACE = ', '
		msg = MIMEMultipart()
		msg['From'] = sender
		msg['To'] = COMMASPACE.join(receivers)
		msg['Subject'] = subject
		body = "Drishti - Vision for life generated Caption"

		msg.attach(MIMEText(body, 'plain'))

	# Attaching Video
		for arg in argv:
			filename = arg
			attachment = open(arg, "rb")
			part = MIMEBase('application', 'octet-stream')
			part.set_payload((attachment).read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
			msg.attach(part)

	# Configuring Server
		text = msg.as_string()
		server.sendmail(sender, receivers, text)
		#server.quit()
if __name__=='__main__':
	obj = email()
	
