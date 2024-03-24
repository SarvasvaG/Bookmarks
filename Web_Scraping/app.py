from TextExtraction import *
from TextSummarizer import *

url=input("\nEnter the url:\n")
extracted_text = extract_text(url)
extracted_text = truncate(extracted_text)
print(extracted_text+"\n")
    
chunks = get_chunks(extracted_text)
summary = get_summary(chunks)
print(summary)