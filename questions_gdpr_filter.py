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
    prompt_template = """Answer the question based on Text in trippleticks. Answer should be yes/no. 
    Give an explanation. Don't reformulate any other question. Restrict to the text given.
    Question : Does the provided question in triple backticks is about the data sharing or exchange of information regulations?
    Text : {question}"""

    prompt = PromptTemplate.from_template(template=prompt_template)
    prompt_formatted_str = prompt.format(question=question)  # Pass the individual question here
    llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])
    prediction = llm.predict(prompt_formatted_str)
    # print the prediction
    #print(prediction)
    return prediction

# Load the Excel file
df = pd.read_excel("./final_excel_files/DataAct.xlsx")

chat_history=[]
for question in df['Competency question']:
    # Prompt the user for a question.
    datasharing = answer_question(question)
    # Print the answer.
    print(question,datasharing)
    chat_history.append((question, datasharing)) 
df_chat_history = pd.DataFrame(chat_history, columns=['Question','Data sharing related ?'])
print(df_chat_history)
df_chat_history.to_excel('data_act_filtered.xlsx', index=False)
