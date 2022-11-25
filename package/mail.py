import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class mail():
    def __init__(self):
        self.server = smtplib.SMTP('198.12.124.54', 25)
        self.server.login("no-reply", "Eggman264.")
        self.server.ehlo
        self.server.starttls
        self.me = "mail@passme.fun"
        with open (textfile, 'rb') as fp:
            self.msg = MIMEText(fp.read())
        
        self.msg['From'] = self.me
    
    def sendMail(self, to, subject, message):
        self.msg['Subject'] = subject
        self.msg['To'] = to
        self.msg['Text'] = message

        self.server.sendmail(self.me, to, self.msg.as_string())
        self.server.quit()