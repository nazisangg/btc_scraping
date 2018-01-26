from bs4 import BeautifulSoup
import requests
import sys

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

    def findAllByAttributes(self):
        targetInformationDic = {}
        for i, x in enumerate(self.findAllByTagName()):
            targetInformationDic[i] = x.attrs[self.tragetAttribute]
        return targetInformationDic

    def main(self):
        targetInformationDic = self.findAllByAttributes()
        print(targetInformationDic)




if __name__ == "__main__":
    ws = Web_Scraping("https://docs.google.com/document/d/17KteJomxBf23oX_FglpVvpD1NeGWjBMjiyD1ldhxmPU/edit", "a", "href")
    ws.main()
