from bs4 import BeautifulSoup
import requests
import sys
from MsgBuilder import MsgBuilder
from smtpGmail import SMTPGmail
from bestLogical import BestLogical


'''URL -> HTML -> Tree'''
'''
    After testing, it can be calimed that the tree can be searched according to the HTML layers.
    which means that we need a tree search to find the tag
'''
class Web_Scraping(object):
    def __init__(self, URL, targetTag, tragetAttribute):
        self.URL = URL
        self.tree = BeautifulSoup(requests.get(URL).text, "html5lib")
        self.targetTag = targetTag
        self.tragetAttribute = tragetAttribute
        self.exchangeName = []
        self.exchangeContent = {}

    def setURL(self, URL):
        self.URL = URL

    def getURL(self):
        return self.URL

    def getTree(self):
        return self.tree

    def getHTMLfromURL(self):
        html = requests.get(self.URL)
        return html.text

    def convertHTMLtoBSTree(self):
        self.tree = BeautifulSoup(self.getHTMLfromURL(), "html5lib")

# TODO need to be updated with other functions
    def treeSearch(self,tree):
        for child in tree.children:
            print("itisc: " + child)
        return tree.children

    def findAllByTagName(self):
        return self.tree.find_all(self.targetTag)

    def findAllByAttributes_exchangeName(self):
        targetInformationDic = []
        for x in self.findAllByTagName():
            try:
                targetInformationDic.append(x.attrs[self.tragetAttribute])
            except(KeyError):
                pass
        self.exchangeName = targetInformationDic

    def findAllByAttributes_brotherSearch(self):
        temExchangeName = self.exchangeName
        bitconName = ''
        #print(temExchangeName)
        for x in self.findAllByTagName():
            targetInformationDic = {}
            #print(temExchangeName[0])
            if x.has_attr("id"):
                exchangename = x['id']
                print('exchangename:', exchangename)
                total_dic = {}
                try:
                    while(x.find_next(self.targetTag).has_attr("id")!=True):
                        #print("1: ",x.find_next(self.targetTag))
                        for m in x.find_next(self.targetTag).find_all("td"):
                            if self.assginTileToPrice(m):
                                #print('here')
                                bitconName = m.text
                            if m.has_attr('class'):
                                #print(m['class'])
                                if m['class'].count('price') == 1:
                                    dic = {bitconName:m.text.split('$')[1]}
                                    total_dic.update(dic)
                                #print(total_dic)
                        x = x.find_next(self.targetTag)
                        self.exchangeContent[exchangename] = total_dic
                        #print(self.exchangeContent)
                        #print('x is: ', x)
                except(AttributeError):
                    pass


    def isAllAppha(self, string):
        argument = True
        list = string.split()
        if string == '':
            argument = False
        if string == 'Total':
            argument = False
        for x in list:
            if (x.isalpha() != True):
                argument = False
        return argument


    def assginTileToPrice(self, tag):
        argument = False
        if(self.isAllAppha(tag.text)):
            #print('name: ', tag.text)
            argument = True
        return argument


    def findOption(self):
        bestlogical = BestLogical(self.exchangeContent)
        bestlogical.dicIntoCheckModel()
        exchangesOverLimit = bestlogical.get_finalDic()
        text = ''
        for conName, value in  exchangesOverLimit.items():
            text = text +'\n'+ "the coin named: " + conName + ' ,highest exchange: ' + value[0] +' ,lowest exchange: ' + value[1] + ' ,difference:'+ str(value[2])
        self.messagesender(text)




    def messagesender(self, text):
        sender = 'nazisang@gmail.com'
        receiver = 'nazisang@gmail.com'
        subject = 'test'
        msgclass = MsgBuilder()
        msgclass.msg_init(sender, receiver, subject)
        msgclass.msg_text(text)
        msg = msgclass.get_msg()
        server = 'smtp.gmail.com'
        username = 'nazisang@gmail.com'
        password = 'summer1993'
        smtp = SMTPGmail(server, username, password)
        smtp.SMTPlogin()
        smtp.sendMail(sender, receiver, msg)

    # 从已经爬得得dict 中拿出一个 exchange得名字，



    def main(self):
        targetInformationDic = self.findAllByAttributes()
        tree = self.tree.find_all("tbody")
#        for x in targetInformationDic.items():






if __name__ == "__main__":
    ws = Web_Scraping("https://coinmarketcap.com/exchanges/volume/24-hour/all/", "tr", "id")
    ws.findAllByAttributes_exchangeName()
    ws.findAllByAttributes_brotherSearch()
    ws.findOption()





