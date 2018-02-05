# btc_scraping
This is a project of web scraping for btc exchanges and prices compare

### Scrabing Part:
This part is mainly finished under BeautifulSoup and request library;
- request:
 - requests.get(URL).text convert html from URL location

- BeautifulSoup:
 - tree = BeautifulSoup(requests.get(URL).text, "html5lib")
  - turn the html into a tree with tags
 - self.tree.find_all(self.targetTag)
  - find all tags under same tag name
 - x.find_next()
  - find all tags with <b>same</b> level in the tree
 - tag.has_attr()
  - check if tag has a attribute named ..., I used this function to distiguish which is correct tag among tags with same tage name

- others
 - x.isalpha()
  - check if the value only contains English characters
 - bitconName:m.text.split('$')[1]
  - I think there is a better way to get rid of $

### Email part:
- smtplib:
 - smtplib.SMTP()
 - self.smtp.connect(self.server, 587)
  - I have tried 25, 467 and 587 port. Only 587 for tls is connected, 467 for ssh is not work
 - self.smtp.ehlo()
 - self.smtp.login(self.username, self.password)
 - self.smtp.sendmail(sender, receiver, msg.as_string())
 - self.smtp.quit()
### massage part:
- from email.mime.multipart import MIMEMultipart
- from email.mime.text import MIMEText
- from email.mime.image import MIMEImage  
 - self.msg = MIMEMultipart('mixed')
 - self.msg['To'] = receiver
 - self.msg['From'] = sender
 - self.msg['Subject'] = subject
 - text_plain = MIMEText(text, 'plain', 'utf-8')
