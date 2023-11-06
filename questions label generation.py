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

embedding = OpenAIEmbeddings()

from langchain.prompts import PromptTemplate


def answer_question(question: str):
    prompt_template = """For the given question, generate a short title of maximum 3 to 4 words. Title should be without "GDPR" word. Output should be only the title.
Question:```{question}```
Title:<Short title for the question>"""

    prompt = PromptTemplate.from_template(template=prompt_template)

    prompt_formatted_str = prompt.format(question=question)
    
    llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])
    
    prediction = llm.predict(prompt_formatted_str)

    # print the prediction
    print(prediction)
    return prediction

# Load the Excel file
df = pd.read_excel("chat_history.xlsx",sheet_name="NO_answers")

questions = df['Question']
chat_history=[]
for question in questions:
    # Prompt the user for a question.
    title = answer_question(question)

    # Print the answer.
    print(question,title)
    chat_history.append((question, title)) 

df_chat_history = pd.DataFrame(chat_history, columns=['Question','Label'])
print(df_chat_history)
df_chat_history.to_excel('chat_history2.xlsx', index=False)
	