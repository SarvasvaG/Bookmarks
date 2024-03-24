from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
nltk.download('punkt')

checkpoint = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model_s = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

def get_chunks(extracted_text):
  sentences = nltk.tokenize.sent_tokenize(extracted_text)

  length = 0
  chunk = ""
  chunks = []
  count = -1
  for sentence in sentences:
    count += 1
    combined_length = len(tokenizer.tokenize(sentence)) + length

    if combined_length  <= tokenizer.max_len_single_sentence:
      chunk += sentence + " "
      length = combined_length

      if count == len(sentences) - 1:
        chunks.append(chunk.strip())

    else:
      chunks.append(chunk.strip())

      length = 0
      chunk = ""

      chunk += sentence + "\n"
      length = len(tokenizer.tokenize(sentence))
  return chunks


def truncate(extracted_text):
    if(len(extracted_text)>=100000):
        extracted_text=extracted_text[:100000]
        
    return extracted_text


def get_summary(chunks):
    inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]
    summary=""
    for input in inputs:
        output = model_s.generate(**input)
        summary+=tokenizer.decode(*output, skip_special_tokens=True)+" "
    return summary
