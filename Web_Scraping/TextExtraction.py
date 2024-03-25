import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840 Safari/537.36'}

class WebScrapper:

    def fetchAndSaveToFile(self, url, path):
        r = requests.get(url, headers=headers)
        with open(path, 'w') as f:
            f.write(r.text)

    def isIrrelevant(self, element):
        irrelevant_tags = ['header', 'footer', 'aside', 'nav']                
        for tag in irrelevant_tags:
            if element.find_parents(tag):
                return True
        return False

    # Title
    def getTitle(self, soup, path):
        title_return=""
        with open(path, 'w', encoding='utf-8') as f:
            title = soup.title
            if title is not None:
                title_text = title.get_text().strip()
                if title_text and any(char.isalnum() for char in title_text):
                    f.write(title_text)
                    f.write('\n')
                    
                    title_return+=title_text+"\n"
        return title_return
            

    # Links
    def getLinkText(self, soup, path):
        link_return=""
        with open(path, 'w', encoding='utf-8') as f:
            links = soup.find_all('a')
            for link in links:
                if not self.isIrrelevant(link):
                    link_text = link.get_text().strip()
                    if link_text and any(char.isalnum() for char in link_text):
                        f.write(link_text)
                        f.write('\n')
                        
                        link_return+=link_text+"\n"
        return link_return

    # li-tag
    def getListTagText(self, soup, path):
        list_return=""
        with open(path, 'w', encoding='utf-8') as f:
            allList = soup.find_all('li')
            for list in allList:
                if not self.isIrrelevant(list):
                    list_text = list.get_text().strip()
                    if list_text and any(char.isalnum() for char in list_text):
                        f.write(list_text)
                        f.write('\n')
                        
                        list_return+=list_text+"\n"
        return list_return

    # Paragraphs
    def getParagraphText(self, soup, path):
        para_return=""
        with open(path, 'w', encoding='utf-8') as f:
            allPara = soup.find_all('p')
            for para in allPara:
                if not self.isIrrelevant(para):
                    para_text = para.get_text().strip()
                    if para_text and any(char.isalnum() for char in para_text):
                        f.write(para_text)
                        f.write('\n')
                        para_return+=para_text+"\n"
        return para_return

    # span-tag
    def getSpanTagText(self, soup, path):
        span_return=""
        with open(path, 'w', encoding='utf-8') as f:
            allSpan = soup.find_all('span')
            for span in allSpan:
                if not self.isIrrelevant(span):
                    span_text = span.get_text().strip()
                    if span_text and any(char.isalnum() for char in span_text):
                        f.write(span_text)
                        f.write('\n')
                        
                        span_return+=span_text+"\n"
        return span_return


def extract_text(url):

    res = requests.get(url, headers=headers).content
    soup = BeautifulSoup(res, 'html.parser')
    
    Scrapper = WebScrapper()
    Scrapper.getTitle(soup, './title.txt')
    Scrapper.getLinkText(soup, './link_text.txt')
    extracted_text=Scrapper.getParagraphText(soup, './para.txt')
    Scrapper.getSpanTagText(soup, './span-tag.txt')
    Scrapper.getListTagText(soup, './li-tag.txt')
    
    return extracted_text


# # url = "https://www.geeksforgeeks.org/strassens-matrix-multiplication/"
# url = "https://en.wikipedia.org/wiki/NP-completeness"
# # url = "https://www.theguardian.com/climate-change-and-you/teach-old-soceity-new-tricks"
# # url = "https://www.notion.so/blog/lessons-we-learned-from-launching-notion-ai"
# url = "https://dareobasanjo.medium.com/disruption-comes-to-google-a88d7f32688b"
url = "https://www.youtube.com/watch?v=Y2wrtZPrct8"

print(extract_text(url))

