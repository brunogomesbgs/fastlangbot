from fastapi import FastAPI
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import ElasticVectorSearch
from fastapi.middleware.cors import CORSMiddleware

from config import openai_api_key

embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

db = ElasticVectorSearch(
    elasticsearch_url="http://localhost:9200",
    index_name="elastic-index",
    embedding=embedding,
)
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=1),
    chain_type="stuff",
    retriever=db.as_retriever(),
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {
        "message": "Welcome to Ask a Meditation: post a question to the address /ask about Meditations by Marcus Aurelius"
    }


@app.post("/ask")
def ask(query: str):
    response = qa.run(query)
    return {
        "response": response,
    }
