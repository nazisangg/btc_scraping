from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import time

class MsgBuilder(object):
    def __init__(self):
        self.msg = MIMEMultipart('mixed')


    def get_msg(self):
        return self.msg

    def msg_init(self, sender, receiver, subject):
        self.msg['Subject'] = subject
        self.msg['From'] = sender
        if type(receiver) == str:
            self.msg['To'] = receiver
        elif type(receiver) == list:
            self.msg['To'] = ";".join(receiver)
        else:
            self.msg['To'] = 'nazisang@gmail.com'
        self.msg['Date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def msg_text(self, text):
        text_plain = MIMEText(text, 'plain', 'utf-8')
        self.msg.attach(text_plain)

    def msg_html(self, text):
        text_html = MIMEText(text, 'html', 'utf-8')
        self.msg.attach(text_html)

    def msg_image(self,url):
        sendimagefile = open(url, 'rb').read()
        image = MIMEImage(sendimagefile)
        image.add_header('Content-ID', '<image1>')
        image["Content-Disposition"] = 'attachment; filename= name'
        self.msg.attach(image)