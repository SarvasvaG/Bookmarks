from text_extract import *
from text_summarize import *

class Summarizer:
    def __init__(self):
        self.text_summarization_tool = TextSummarizer()
        self.text_extraction_tool = TextExtraction()
    
    
    def summarize(self, url):
        extracted_text = self.text_extraction_tool.extract_text(url)
        extracted_text = self.text_summarization_tool.truncate(extracted_text)
        chunks = self.text_summarization_tool.get_chunks(extracted_text)
        summary = self.text_summarization_tool.get_summary(chunks)
        
        return summary
    
url = input("Enter the url:\n")
print(Summarizer().summarize(url))