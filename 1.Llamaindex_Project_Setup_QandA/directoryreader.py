#from llama_index.readers.web import SimpleDirectoryReader
#from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import os
from dotenv import load_dotenv
#import logging
import sys

load_dotenv()

def main(url:str)->None:
    documents = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query('genai?')
    print(response)

if __name__ == '__main__':
    #loading data from my local machine
    main(url="C:\\Users\\Asus-2020\\Downloads\\data")
