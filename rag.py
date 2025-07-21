from dotenv import load_dotenv
from prompt import prompt, example_prompt
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from pathlib import Path
from uuid import uuid4

load_dotenv()

llm = None
vector_store=None

def initialize_components():
    global llm, vector_store
    vectordbdir = Path(__file__).parent / "resources/vectordb"

    if llm is None:
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.9, max_tokens=500)

    if vector_store is None:
        ef = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'trust_remote_code':True})
        vector_store = Chroma(collection_name="real_estate", embedding_function=ef, persist_directory=str(vectordbdir))

def process_urls(urls):

    yield "Initializing components LLM and Vector Database..."
    initialize_components()

    yield "Loading data..."
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    yield "Splitting text into chunks..."
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, separators=["\n\n", "\n", " ", "."])
    docs = text_splitter.split_documents(data)

    yield "Adding chunks to vector database..."
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(docs, ids=uuids)

    yield "Done adding docs to vector database."

def generate_answer(question):
    if not vector_store:
        raise RuntimeError("Vector database is not initialized.")
    qa_chain = load_qa_with_sources_chain(llm, chain_type="stuff", prompt=prompt, document_prompt=example_prompt)
    chain = RetrievalQAWithSourcesChain(combine_documents_chain=qa_chain, retriever=vector_store.as_retriever(),
                                        reduce_k_below_max_tokens=True, max_tokens_limit=8000, return_source_documents=True)
    result = chain.invoke({"question":question}, return_only_outputs=True)
    source_docs = [doc.metadata["source"] for doc in result["source_documents"]]
    source_docs = list(set(source_docs))

    return result["answer"], source_docs


# urls = ["https://www.thehindubusinessline.com/news/real-estate/brigade-explores-industrial-push-amid-tech-driven-real-estate-demand/article69834419.ece",
# "https://www.businesstoday.in/personal-finance/real-estate/story/indias-middle-class-buying-liabilities-real-estate-advisor-shows-how-rich-turn-property-into-profit-485435-2025-07-21"]
#
#what is value migration model?
#which city has high pharma demand and in which year?
#which city has high BFSI demand?

