import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class WebScrapper:

    def fetchAndSaveToFile(self, url, path):
        r = requests.get(url, headers=headers)
        with open(path, 'w') as f:
            f.write(r.text)

    def isIrrelevant(self, element):
        irrelevant_tags = ['header', 'footer', 'aside', 'nav']                 # Add more irrelevant tags if needed
        for tag in irrelevant_tags:
            if element.find_parents(tag):
                return True
        return False

    # Title
    def getTitle(self, soup, path):
        with open(path, 'w', encoding='utf-8') as f:
            title = soup.title
            title_text = title.get_text().strip()
            if title_text and any(char.isalnum() for char in title_text):
                f.write(title_text)
                f.write('\n')

    # Links
    def getLinkText(self, soup, path):
        with open(path, 'w', encoding='utf-8') as f:
            links = soup.find_all('a')
            for link in links:
                if not self.isIrrelevant(link):
                    link_text = link.get_text().strip()
                    if link_text and any(char.isalnum() for char in link_text):
                        f.write(link_text)
                        f.write('\n')

    # li-tag
    def getListTagText(self, soup, path):
        with open(path, 'w', encoding='utf-8') as f:
            allList = soup.find_all('li')
            for list in allList:
                if not self.isIrrelevant(list):
                    list_text = list.get_text().strip()
                    if list_text and any(char.isalnum() for char in list_text):
                        f.write(list_text)
                        f.write('\n')

    # Paragraphs
    def getParagraphText(self, soup, path):
        with open(path, 'w', encoding='utf-8') as f:
            allPara = soup.find_all('p')
            for para in allPara:
                if not self.isIrrelevant(para):
                    para_text = para.get_text().strip()
                    if para_text and any(char.isalnum() for char in para_text):
                        f.write(para_text)
                        f.write('\n')

    # span-tag
    def getSpanTagText(self, soup, path):
        with open(path, 'w', encoding='utf-8') as f:
            allSpan = soup.find_all('span')
            for span in allSpan:
                if not self.isIrrelevant(span):
                    span_text = span.get_text().strip()
                    if span_text and any(char.isalnum() for char in span_text):
                        f.write(span_text)
                        f.write('\n')


def getContent(url):

    res = requests.get(url, headers=headers).content
    soup = BeautifulSoup(res, 'html.parser')
    # print(soup.prettify())
    
    Scrapper = WebScrapper()

    # Scrapper.fetchAndSaveToFile(url, './website.html')
    Scrapper.getTitle(soup, './title.txt')
    Scrapper.getLinkText(soup, './link_text.txt')
    Scrapper.getParagraphText(soup, './para.txt')
    Scrapper.getSpanTagText(soup, './span-tag.txt')
    Scrapper.getListTagText(soup, './li-tag.txt')


# url = "https://www.geeksforgeeks.org/strassens-matrix-multiplication/"
# url = "https://en.wikipedia.org/wiki/NP-completeness"
# url = "https://www.theguardian.com/climate-change-and-you/teach-old-soceity-new-tricks"
# url = "https://www.notion.so/blog/lessons-we-learned-from-launching-notion-ai"
url = "https://dareobasanjo.medium.com/disruption-comes-to-google-a88d7f32688b"

getContent(url)

