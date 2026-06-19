from src.helper import load_pdf, text_split, embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
import os

load_dotenv()
pinecone_api_key=os.getenv("PINECONE_API_KEY")

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)


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

docsearch = PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name = index_name)