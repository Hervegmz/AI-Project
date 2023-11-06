import os

import streamlit as st
from dotenv import find_dotenv, load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader, UnstructuredPDFLoader
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from loguru import logger

import pandas as pd
_ = load_dotenv(find_dotenv())
os.environ["OPENAI_API_KEY"] =  "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" #dr mansoor key #

persist_directory ="aiact_excluding_footer_db"
embedding = OpenAIEmbeddings()

'''
import fitz # imports the pymupdf library
import re


doc = fitz.open("AI Act.pdf") 

def identify_footer_line(text):
  """Identifies the horizontal line separating the footer of the page in Python while extracting text.

  Args:
    text: The text to be extracted.

  Returns:
    The index of the horizontal line separating the footer of the page, or -1 if the line cannot be identified.
  """

  # Regular expression to match the horizontal line.
  horizontal_line_regex = r'                                                 '

  # Search for the horizontal line in the text.
  match = re.search(horizontal_line_regex, text)

  # If the horizontal line is found, return its index.
  if match:
    return match.start()

  # Otherwise, return -1.
  else:
    return -1   
  

def extract_text_without_footer(text):
  """Extracts the text from the given text, excluding the page footer text.

  Args:
    text: The text to be extracted.

  Returns:
    The extracted text, without the page footer text.
  """

  # Identify the horizontal line separating the footer of the page.
  footer_line_index = identify_footer_line(text)

  # If the horizontal line is found, extract the text before the line.
  if footer_line_index != -1:
    extracted_text = text[:footer_line_index]
    extracted_text = re.sub(r'EN.+EN', '', extracted_text,flags=re.DOTALL).strip()
  # Otherwise, extract the entire text.
  else:
    extracted_text = text

  return extracted_text

#print(extract_text_without_footer(doc[19].get_text()))

#lines = extract_text_without_footer(doc[19].get_text()).splitlines()
#document_text = ''.join([line.strip() for line in lines])
#documents = re.split(r"\.", document_text)

#print(documents)
#print(len(documents))
document_text = ""
for page in doc: # iterate the document pages
  page_content = page.get_text()
  if page.number < 97:
      #lines = extract_text_without_footer(page_content).splitlines() # get plain text encoded as UTF-8
      page_text = extract_text_without_footer(page_content)#' '.join([line.strip() for line in lines])
      page_text = re.sub(r'EN.+EN', '', page_text,flags=re.DOTALL).strip()
      document_text = document_text.strip()+' '+page_text.strip()
      


documents = re.split(r'\D\. \n',document_text.strip())
vectordb = Chroma.from_texts(
texts=documents,
embedding=embedding,
persist_directory=persist_directory,
)
vectordb.persist()

'''
# load existing db
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    

def answer_question(question: str):

    q_rs = vectordb.similarity_search(question, k=1)
    #print(q_rs[0].page_content) 
    answer = load_qa_chain(ChatOpenAI(model="gpt-4",temperature=0.2), chain_type="stuff").run(input_documents=q_rs, question=question)
    return answer
    #return q_rs[0].page_content

# Load the Excel file
df = pd.read_excel(".\Excel\questions_compliance.xlsx",sheet_name="questions_GDPR_filtered")

statements = df['Question'].to_list()
chat_history=[]
for statement in statements:
# Prompt the user for a YES/NO answer
  question = f"""As a experienced compliance analyst. Restrict to given context while answering the question. Answer only in yes/no. Provide separately the explanation for the answer. Don't consider GDPR regulations while answering the question.
  Question:```{statement}```
  Answer:<yes/no>
  Explanation:<explanation of the answer>"""
  # Prompt the user for a question.
  answer = answer_question(question)
  print(answer)
  chat_history.append((statement, answer)) 

df_chat_history = pd.DataFrame(chat_history, columns=['Statement','YES/NO answer'])
print(df_chat_history)
df_chat_history.to_excel('chat_history.xlsx', index=False)


