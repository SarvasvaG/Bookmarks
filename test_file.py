from text_extraction import TextExtraction
import asyncio

web = ['https://www.notion.so/blog/how-to-calculate-your-companys-ai-roi-for-real']

async def main():

    text_extraction = TextExtraction()
    useful_word_lists = await text_extraction.extract_text(web)

    for url, useful_words in zip(web, useful_word_lists):
        print(useful_words)

asyncio.run(main())