import asyncio
import aiohttp
import bs4
import spacy
from urllib.parse import urlparse

class ScrapTool:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    async def visit_url(self, session, website_url):
        try:
            async with session.get(website_url, timeout=60) as response:
                if response.status == 403:                              # Check if access is forbidden
                    print(f"Access to {website_url} is forbidden.")
                    return {"website_url": website_url, "website_text": "Blocked"}
                content = await response.read()
                soup = bs4.BeautifulSoup(content, "lxml")
                return self.process_soup(soup)
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            print(f"Error accessing {website_url}: {e}")
            return None

    def process_soup(self, soup):
        website_text = self.get_text_content(soup)
        return website_text

    def get_text_content(self, soup):
        tags_to_ignore = ['style', 'script', 'head', 'title', 'meta', '[document]', "h1", "h2", "h3", "h4", "h5", "h6", "noscript"]
        tags = soup.find_all(lambda tag: tag.name not in tags_to_ignore)
        result = []
        for tag in tags:
            if isinstance(tag, bs4.element.Comment) or not tag.text.strip():
                continue
            result.append(tag.get_text(strip=True))
        return ' '.join(result)

    async def extract_website_text(self, urls):
        async with aiohttp.ClientSession() as session:
            tasks = [self.visit_url(session, url) for url in urls]
            results = await asyncio.gather(*tasks)
            return results

class TextExtraction:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_useful_words(self, doc):
        doc = self.nlp(doc)
        useful_words = [token.text.lower().strip() for token in doc if not token.is_stop and not token.is_punct and not token.text.isnumeric() and token.text.isalnum()]

        useful_words = ' '.join(useful_words)
        # print(type(useful_words))

        return useful_words

    async def extract_text(self, website_urls):
        scrap_tool = ScrapTool()
        website_texts = await scrap_tool.extract_website_text(website_urls)
        useful_word_lists = []
        for website_text in website_texts:
            if website_text and isinstance(website_text, str):
                useful_word_lists.append(self.extract_useful_words(website_text))
            else:
                useful_word_lists.append(['Blocked'])
        
        # print(type(useful_word_lists))
        # print(len(useful_word_lists))
        
        return useful_word_lists

async def main():

    website_urls = []
    url = input("Enter a website URL (leave blank to stop): ").strip()
    if not url:
        print("No URLs provided. Exiting.")
    website_urls.append(url)

    text_extraction = TextExtraction()
    useful_word_lists = await text_extraction.extract_text(website_urls)
    # print(type(useful_word_lists))

    for url, useful_words in zip(website_urls, useful_word_lists):
        print(f"Useful words extracted from {url}:\n{useful_words}\n")

if __name__ == "__main__":
    asyncio.run(main())

