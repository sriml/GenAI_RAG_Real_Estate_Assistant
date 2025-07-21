# GenAI-RAG RealEstate Research Assistant

Aim of the project: Generate Coherent answers based on the given real-estate specific knowledge URLs.

Technical Architecture: 
 - Input documents (as URLs) are provided to Langchain URLLoader 
 - Split the content of documents into chunks by Langchain text splitter
 - Chunks are transformed into Embedding vectors by HuggingFace Embedding Model
 - Embedding vectors are stored into Vector database (Langchain Chroma)
 - Relevant chunks based on the input query are retrieved and along with Prompt are input to Groq LLM
 - LLM generates answer (LLama model is used here)


