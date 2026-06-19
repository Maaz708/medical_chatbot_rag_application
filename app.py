from flask import Flask, render_template, jsonify, request
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
import os

from src.prompt import *

app=Flask(__name__)

load_dotenv()
pinecone_api_key=os.getenv("PINECONE_API_KEY")

#create embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-large-en-v1.5",
    )

pc=Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot-rag"


if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension =1024,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )

    )

index=pc.Index("medical-chatbot-rag")

docsearch = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template = promt_template
)
chain_type_kwargs = {"prompt":prompt}

llm = ChatOllama(
    model = "gemma3:4b",
    max_new_tokens = 512,
    temperature=0.8
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever = docsearch.as_retriever(search_kwargs={'k':2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()

    msg = data["msg"]

    print("User:", msg)

    result = qa.invoke({"query": msg})

    print("Response:", result["result"])

    return jsonify({
        "response": result["result"]
    })

if __name__ == '__main__':
    app.run(debug=True)