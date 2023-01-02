import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class mail():
    def __init__(self):
        self.server = smtplib.SMTP('passme.fun', 25)
        self.server.starttls()
      #  self.server.connect
       # self.server.login("no-reply", "Egg.man264.")
        self.me = "mail@passme.fun"
      #  with open (textfile, 'rb') as fp:
       #      self.msg = MIMEText(fp.read())
        self.msg = MIMEText("test")
        
        self.msg['From'] = self.me
    
    def sendMail(self, to, subject, message):
        self.msg['Subject'] = subject
        self.msg['To'] = to
        self.msg['Text'] = message

        self.server.sendmail(self.me, to, self.msg.as_string())
        self.server.quit()


