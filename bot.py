from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st 

st.title("Dark Chatbot")
input_qry = st.text_input("Enter your queries..")

prompt = ChatPromptTemplate([
        ("system", "You are a healpful AI assistant. You name is Dark Assistant"),
        ("User query: {query}")
    ])

llm = Ollama(model = "llama2")
out_parser = StrOutputParser()
chain = prompt|llm|out_parser

if input_qry:
    st.write(chain.invoke({'query':input_qry}))