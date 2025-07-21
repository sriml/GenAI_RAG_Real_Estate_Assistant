# GenAI-RAG Real Estate Research Assistant

Aim of the project: Generate coherent answers based on the given real-estate specific knowledge URLs.

## Technical Architecture: 
 - Input documents (as URLs) are provided to Langchain URLLoader 
 - Split the content of documents into chunks by Langchain text splitter
 - Chunks are transformed into Embedding vectors by HuggingFace Embedding Model
 - Embedding vectors are stored into Vector database (Langchain Chroma)
 - Relevant chunks based on the input query are retrieved and along with Prompt are input to Groq LLM
 - LLM generates answer (LLama model is used here)

<img width="1690" height="1021" alt="image" src="https://github.com/user-attachments/assets/6b7a5c70-3490-4106-9c1b-2fd2cdbf85be" />

<img width="1660" height="867" alt="image" src="https://github.com/user-attachments/assets/2e3358b0-3c89-4d85-846f-a8a6a2d4593b" />

<img width="1624" height="760" alt="image" src="https://github.com/user-attachments/assets/5a02af1f-e79e-4adb-befa-71885f043ad7" />



