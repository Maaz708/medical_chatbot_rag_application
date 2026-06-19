# Medical Chatbot RAG Application

## Overview

Medical Chatbot RAG APPlication is a Retrieval-Augmented Generation (RAG) based Medical Chatbot built using Flask, LangChain, Pinecone, Hugging Face Embeddings, and Ollama.

The chatbot allows users to ask medical questions and receive answers generated from a custom knowledge base stored in Pinecone.

---

## Features

* Retrieval-Augmented Generation (RAG)
* Semantic Search using Pinecone Vector Database
* Hugging Face Embeddings
* Local LLM inference using Ollama
* Flask Web Interface
* PDF-based Knowledge Base

---

## Tech Stack

## Tech Stack

* Python
* Langchain
* Flask
* Ollama
* Pinecone

### Embeddings

* BAAI/bge-large-en-v1.5

### Large Language Model

* Gemma 3 (4B) via Ollama

### Screenshot

<img width="1607" height="612" alt="Screenshot 2026-06-19 172539" src="https://github.com/user-attachments/assets/f4fcc3ff-79a7-45f0-bddc-182af800205a" />





## Project Structure

```text
medical-chatbot-rag/
│
├── app.py
├── requirements.txt
├── .env
│
├── templates/
│   └── chat.html
│
├── static/
│   ├── style.css
│
├── src/
│   ├── prompt.py
│   ├── helper.py
│
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd medical-chatbot-rag
```

## To run the code

## step -1

```bash
clone the repository
```


```bash 
create virtual environment
python -m venv venv
```
```bash
Activate the virtual environment
venv/Scripts/Activate
```
## Create a '.env' file in the root directory and add your Pinecone credential
```bash
PINECONE_API_KEY=""

```


## Step 2- Install the requirements

```bash
 pip install -r requirements.txt

```

## Step 3- Store the data in Pinecone

```bash
python store_index.py
```

## Step 4- Run the flask app

```bash
python app.py
```



## Install Ollama

Download and install Ollama:

https://ollama.com

Pull the Gemma model:

```bash
ollama pull gemma3:4b
```

Start Ollama:

```bash
ollama serve
```

Verify installation:

```bash
ollama list
```

---

## Pinecone Setup

Create a Pinecone account and obtain an API key.

The application automatically creates an index:

```text
medical-chatbot-rag
```

Configuration:

```python
dimension = 1024
metric = "cosine"
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Workflow

```text
User Question
      │
      ▼
Hugging Face Embeddings
      │
      ▼
Pinecone Vector Search
      │
      ▼
Relevant Chunks Retrieved
      │
      ▼
LangChain RetrievalQA
      │
      ▼
Gemma 3 via Ollama
      │
      ▼
Response Returned
      │
      ▼
Displayed in Chat UI
```



## Future Improvements

* Chat History Memory
* Source Citation Display
* Streaming Responses
* User Authentication
* PDF Upload Interface
* Multi-Document Retrieval
* Conversation Context Retention


## Author

Mohd Maaz

Built as a Retrieval-Augmented Generation (RAG) Medical Chatbot using Flask, LangChain, Pinecone, Hugging Face Embeddings, and Ollama.















