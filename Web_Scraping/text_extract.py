import requests
from bs4 import BeautifulSoup

class WebScrapper:
    def isIrrelevant(self, element):
        irrelevant_tags = ['header', 'footer', 'aside', 'nav']                
        for tag in irrelevant_tags:
            if element.find_parents(tag):
                return True
        return False

    def getParagraphText(self, soup):
        para_return=""
        allPara = soup.find_all('p')
        for para in allPara:
            if not self.isIrrelevant(para):
                para_text = para.get_text(separator=' ', strip=True).replace('\n', ' ')
                if para_text and any(char.isalnum() for char in para_text):

                    para_return+=para_text+"\n"
        return para_return

class TextExtraction():
    def __init__(self):
        self.scrapper = WebScrapper()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840 Safari/537.36'}
        
    def extract_text(self,url):
        res = requests.get(url, headers=self.headers).content
        soup = BeautifulSoup(res, 'html.parser')
        extracted_text = self.scrapper.getParagraphText(soup)
        return extracted_text
