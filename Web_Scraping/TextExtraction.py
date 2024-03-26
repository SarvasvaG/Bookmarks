import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840 Safari/537.36'}

class WebScrapper:

    def isIrrelevant(self, element):
        irrelevant_tags = ['header', 'footer', 'aside', 'nav']                
        for tag in irrelevant_tags:
            if element.find_parents(tag):
                return True
        return False

    # Paragraphs
    def getParagraphText(self, soup):
        para_return=""
        allPara = soup.find_all('p')
        for para in allPara:
            if not self.isIrrelevant(para):
                para_text = para.get_text(separator=' ', strip=True).replace('\n', ' ')
                if para_text and any(char.isalnum() for char in para_text):

                    para_return+=para_text+"\n"
        return para_return

def extract_text(url):

    res = requests.get(url, headers=headers).content
    soup = BeautifulSoup(res, 'html.parser')
    
    Scrapper = WebScrapper()
    extracted_text = Scrapper.getParagraphText(soup)
    
    return extracted_text


# url = "https://www.geeksforgeeks.org/strassens-matrix-multiplication/"
url = "https://en.wikipedia.org/wiki/NP-completeness"
# url = "https://www.theguardian.com/climate-change-and-you/teach-old-soceity-new-tricks"
# url = "https://www.notion.so/blog/lessons-we-learned-from-launching-notion-ai"
# url = "https://dareobasanjo.medium.com/disruption-comes-to-google-a88d7f32688b"
# url = "https://www.youtube.com/watch?v=Y2wrtZPrct8"

print(extract_text(url))

