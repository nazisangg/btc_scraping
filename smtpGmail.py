import smtplib

class SMTPGmail(object):

    def __init__(self, server, username, password):
        self.smtp = smtplib.SMTP()
        self.server = server
        self.username = username
        self.password = password

    def set_server(self, server):
        self.server = server

    def get_server(self):
        return self.server

    def set_username(self, username):
        self.server = username

    def get_username(self):
        return self.username

    def set_passwordr(self, password):
        self.password = password

    def get_passwordr(self):
        return self.password

    def SMTPlogin(self):
        self.smtp.connect(self.server, 587)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()
        self.smtp.login(self.username, self.password)

    def sendMail(self,sender, receiver, msg):
        self.smtp.sendmail(sender, receiver, msg.as_string())
        self.smtp.quit()

