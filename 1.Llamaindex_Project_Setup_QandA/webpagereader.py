#from llama_index.llms import OpenAI
from llama_index.llms.openai import OpenAI
#from llama_index.readers import SimpleWebPageReader
from llama_index.readers.web import SimpleWebPageReader
#from llama_index import VectorStoreIndex
from llama_index.core import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv


load_dotenv()

def main(url: str)-> None:
    #crating the obj of simplewebreader
    document=SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    #pass the document to the vector store index
    index = VectorStoreIndex.from_documents(documents=document)
    #create the query engine
    query_engine = index.as_query_engine()
    response = query_engine.query('History of generative AI?')
    print(response)


if __name__ == "__main__":
    main(url="https://medium.com/@raja.gupta20/generative-ai-for-beginners-part-1-introduction-to-ai-eadb5a71f07d")