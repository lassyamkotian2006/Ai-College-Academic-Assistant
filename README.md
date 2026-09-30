# Ai-College-Academic-Assistant
An intelligent AI-based College Academic Assistant built using LLM, RAG, LangChain, and LangGraph to search college documents, answer student queries, and generate personalized study plans.
# Person 2 – RAG and Answer Generation

## Overview

Person 2 implements the **Retrieval-Augmented Generation (RAG)** part of the AI College Academic Assistant.

The system uses the vector database created by Person 1 to retrieve relevant academic documents and then uses a Gemini language model to generate an answer based on the retrieved context.

## Person 2 Responsibilities

The Person 2 pipeline includes:

1. Loading the embedding model.
2. Loading Person 1's ChromaDB vector database.
3. Taking the user's question as input.
4. Retrieving relevant documents from ChromaDB.
5. Applying a similarity-distance threshold to filter relevant results.
6. Creating context from the retrieved documents.
7. Sending the context and question to the Gemini model.
8. Generating an answer using RAG.
9. Displaying the retrieved source documents along with the generated answer.

## RAG Pipeline

```text
User Question
      ↓
Embedding Model
      ↓
ChromaDB Retrieval
      ↓
Top-K Documents
      ↓
Similarity / Distance Filtering
      ↓
Relevant Documents
      ↓
Context Creation
      ↓
Gemini LLM
      ↓
Generated Answer
```

## Embedding Model

The project uses a Sentence Transformer embedding model to represent the user's question and academic documents as vectors.

The embedding model is used for semantic retrieval rather than simple keyword matching.

## ChromaDB

Person 2 loads the **ChromaDB vector database created by Person 1**.

The database contains academic content such as:

* Course syllabi
* Notes
* Question banks
* MCQs
* College rules and FAQs
* Other academic resources

Relevant documents are retrieved based on semantic similarity to the user's question.

## Retrieval and Filtering

For each query, the system retrieves the top relevant documents.

A distance threshold is then used to remove results that are not sufficiently relevant.

Example:

```text
Query:
What are the units in Object Oriented Programming?

Retrieved:
5 documents

Relevant after filtering:
2 documents
```

This helps provide the language model with more relevant context.

## Context Creation

The relevant retrieved documents are combined into a context that is passed to the Gemini model.

The context contains information such as:

* Document source
* Retrieved content
* Similarity distance

This allows the model to generate an answer using the academic documents retrieved from ChromaDB.

## Gemini Integration

The project uses Google's Gemini model through LangChain.

The Gemini API key is stored securely using **Google Colab Secrets** rather than directly writing the API key inside the notebook.

Example:

```python
from google.colab import userdata

GOOGLE_API_KEY = userdata.get("Google_API_key")
```

The API key should **never be uploaded to GitHub**.

## Example Query

```text
What are the units in Object Oriented Programming?
```

The retrieval system identifies relevant OOP syllabus content from the ChromaDB database and provides it as context to the Gemini model.

## Technologies Used

* Python
* Google Colab
* ChromaDB
* Sentence Transformers
* LangChain
* Google Gemini
* RAG (Retrieval-Augmented Generation)

## Output

The final system provides:

* User question
* Retrieved relevant documents
* Source information
* AI-generated answer based on the retrieved academic context



Person 1 provides the academic data, embeddings, and ChromaDB vector store, while Person 2 uses these components to build the RAG-based question-answering system.
